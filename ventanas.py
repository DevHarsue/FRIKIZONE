from interfaz.configuracion import Ui_VentanaConfiguracion
from interfaz.login.ui_ventana4 import Ui_VentanaRegistro
from interfaz.message import Ui_Message
from interfaz.question import Ui_Question
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow,QDialog
from Hilos.prueba_env import HiloEnv
from Validacion.validador import Validador
from Validacion.hash import texto_a_hash,texto_a_hash_salt
from conexion_bd.tablas import TablaUsuarios

class VentanaConfiguracion(QMainWindow):
    def __init__(self, ventana):
        super().__init__()
        self.ventana = ventana
        self.ui = Ui_VentanaConfiguracion()
        self.ui.setupUi(self)
        self.ui.boton_conectar.pressed.connect(self.conectar)
        self.ui.boton_volver.pressed.connect(self.regresar)
        self.env = False
        self.mensaje = Mensaje()
        validador = Validador()
        validador.cedulas(self.ui.line_port)
    
    def conectar(self):
        usuario = self.ui.line_usuario.text()
        contraseña = self.ui.line_contrasena.text()
        host = self.ui.line_host.text()
        puerto = self.ui.line_port.text()
        if puerto=="" or usuario=="" or host=="":
            self.mensaje.mostrar("Error", "Por favor ingrese todos los datos")
            return 0
        puerto = int(puerto)
        if self.env:
            return 0
        self.env = HiloEnv(usuario,contraseña,host,puerto)
        self.env.status.connect(self.respuesta)
        self.env.start()
        self.cambiar_estado(False)
    
    def respuesta(self,respuesta):
        if respuesta:
            self.mensaje.mostrar("Conexion Exitosa","Conexion a la base de datos exitosa")
            self.env = False
            self.regresar()
            try:
                self.ventana.buscar_usuarios()
            except Exception as e:
                pass
        else:
            self.mensaje.mostrar("Conexion Fallida","No se pudo conectar a la base de datos")
            self.env = False
            self.cambiar_estado(True)
    
    def cambiar_estado(self,bool):
        self.ui.boton_conectar.setEnabled(bool)
        self.ui.line_usuario.setEnabled(bool)
        self.ui.line_contrasena.setEnabled(bool)
        self.ui.line_host.setEnabled(bool)
        self.ui.line_port.setEnabled(bool)
    
    def regresar(self):
        self.ventana.show()
        self.close()
        

class VentanaRegistro(QMainWindow):
    def __init__(self, ventana):
        super().__init__()
        self.ventana = ventana
        self.ui = Ui_VentanaRegistro()
        self.ui.setupUi(self)
        self.validador = Validador()
        self.ui.boton_registrar.pressed.connect(self.registrar)
        self.ui.boton_volver.pressed.connect(self.regresar)
        self.validador.usuarios(self.ui.line_usuario)
        self.mensaje = Mensaje()
        self.pregunta = Preguntar()
        self.respuesta = False
        self.pregunta.respuesta.connect(self.recibir_respuesta)
    
    def recibir_respuesta(self,respuesta):
        self.respuesta = respuesta
    
    def registrar(self):
        usuario = self.ui.line_usuario.text().upper()
        contraseña = self.ui.line_contrasena.text()
        confirmar = self.ui.line_confirmar.text()
        if usuario=="" or contraseña=="" or confirmar=="":
            self.mensaje.mostrar("Error", "Por favor ingrese todos los datos")
            return 0
        
        if len(usuario)<6:
            self.mensaje.mostrar("Error", "El usuario debe tener al menos 6 caracteres")
            return 0
        
        existe = TablaUsuarios().select_usuario(usuario)
        if bool(existe):
            self.mensaje.mostrar("Error", "El usuario ya existe")
            return 0
        
        if not self.validador.comprobar_contraseña(contraseña):
            self.mensaje.mostrar("Contraseña Invalida", "La contraseña debe:\n-Conteneral menos una letra mayuscula y una minuscula\n-Contener dos digitos\n-Contener un caracter especial\n-Ser minima de 8 caracteres")
            return 0
        
        if contraseña!=confirmar:
            self.mensaje.mostrar("Contraseña Invalida", "Las contraseñas no coinciden")
            return 0
        
        rol = self.ui.comboBox.currentText()
        TablaUsuarios().insert(texto_a_hash(usuario),texto_a_hash(contraseña),texto_a_hash_salt(rol))
        self.mensaje.mostrar("Registro Exitoso", "El usuario ha sido registrado con exito")
        if rol!="SUPERADMIN":
            superadmin = TablaUsuarios().select_rol(texto_a_hash_salt("SUPERADMIN"))
            if not bool(superadmin):
                self.mensaje.mostrar("No hay SUPERADMIN", "No existe un SUPERADMIN, Por favor registra uno")
                self.reiniciar()
                return 0
        else:
            self.ui.comboBox.removeItem(0)
            
        self.pregunta.mostrar("Registrar mas usuarios","¿Desea Registrar mas usuarios?")
        if self.respuesta:
            self.reiniciar()
            return 0
        
        self.regresar()        
        
    def reiniciar(self):
        self.ui.line_usuario.setText("")
        self.ui.line_contrasena.setText("")
        self.ui.line_confirmar.setText("")
        self.ui.comboBox.setCurrentIndex(0)
    
    def regresar(self):
        self.ventana.show()
        self.close()
    

class Mensaje(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.ui = Ui_Message()
        self.ui.setupUi(self)
        self.ui.pushButton.pressed.connect(self.close)
    
    def mostrar(self,titulo,mensaje):
        self.ui.pushButton.setDefault(True)
        self.setWindowTitle(titulo)
        self.ui.label.setText(mensaje)
        self.exec_()
        

class Preguntar(QDialog):
    respuesta = Signal(bool)
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.ui = Ui_Question()
        self.ui.setupUi(self)
        self.ui.pushButton.pressed.connect(self.si)
        self.ui.pushButton_2.pressed.connect(self.no)
    
    def mostrar(self,titulo,mensaje):
        self.ui.pushButton.setDefault(True)
        self.setWindowTitle(titulo)
        self.ui.label.setText(mensaje)
        self.exec_()
    
    def si(self):
        self.respuesta.emit(True)
        self.close()
    
    def no(self):
        self.respuesta.emit(False)
        self.close()