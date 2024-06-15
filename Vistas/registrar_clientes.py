from Hilos.cne import HiloCNE
from conexion_bd.tablas import TablaClientes
from Validacion.validador import Validador
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIntValidator

class VistaRegistrarClientes:
    def __init__(self,ventana) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.vista_registrar_clientes()
    
    #Vista Registro Clientes
    def vista_registrar_clientes(self):
        self.tablaClientes = TablaClientes()
        #Coloco el estado principal de checkbox y le agrego el slot
        self.ui.check_editar_rcliente.setChecked(True)
        self.ui.check_editar_rcliente.clicked.connect(self.cambiar_estado_line_nombres)
        
        #Estado inicial de line edits para el nombre
        self.ui.line_nombre_rcliente.setEnabled(False)
        self.ui.line_apellido_rcliente.setEnabled(False)
        
        #se agrega un validador al line edit de cedula para que solo admita numeros
        self.ui.line_cedula_rcliente.setValidator(QIntValidator())
        
        #Conectamos los slots de los botones
        self.ui.boton_buscar_rcliente.clicked.connect(self.buscar_cliente_registro)
        self.ui.boton_registrar_rcliente.clicked.connect(self.registrar_cliente)
    
    def cambiar_estado_line_nombres(self):
        if not self.ui.check_editar_rcliente.isChecked():
            self.ui.line_nombre_rcliente.setEnabled(True)
            self.ui.line_apellido_rcliente.setEnabled(True)
        else:
            self.ui.line_nombre_rcliente.setEnabled(False)
            self.ui.line_apellido_rcliente.setEnabled(False)
    
    def buscar_cliente_registro(self):
        cedula = self.ui.line_cedula_rcliente.text()
        if cedula == "":
            QMessageBox.information(self.ventana,"Cedula vacia","Porfavor ingresa un numero de cedula",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0
        
        persona = self.tablaClientes.select(int(cedula))
        if not bool(persona):
            self.ui.line_apellido_rcliente.setText("Cargando del CNE...")
            self.ui.line_nombre_rcliente.setText("Cargando del CNE...")
            self.hilo_CNE = HiloCNE(self.ui.combo_nacionalidad_rcliente.currentText(),cedula)
            self.hilo_CNE.persona.connect(self.mostrar_cliente_cne)
            self.hilo_CNE.error.connect(self.ventana.mostrar_error)
            self.hilo_CNE.terminar.connect(self.definir_estado)
            self.hilo_CNE.start()
        else:
            QMessageBox.information(self.ventana,"Cliente registrado",f"El cliente ya ha sido registrado como {persona[0].nombre} {persona[0].apellido}",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            
        
    def mostrar_cliente_cne(self,nombre_persona):
        self.ui.line_nombre_rcliente.setText(nombre_persona[0])
        self.ui.line_apellido_rcliente.setText(nombre_persona[1])
    
    def definir_estado(self):
        if self.ui.line_nombre_rcliente.text() == "Cargando del CNE...":
            self.ui.line_apellido_rcliente.setText("")
            self.ui.line_nombre_rcliente.setText("")
            
    def registrar_cliente(self):
        validador = Validador()
        cedula = self.ui.line_cedula_rcliente.text()
        nombre = self.ui.line_nombre_rcliente.text()
        apellido = self.ui.line_apellido_rcliente.text()
        nacionalidad = self.ui.combo_nacionalidad_rcliente.currentText()
        direccion = self.ui.text_descripcion_rcliente.toPlainText()
        numero = self.ui.line_telefono_rcliente.text()
        
        #Aqui deberian ir las validaciones
        persona = self.tablaClientes.select(int(cedula))
        if bool(persona):
            self.ventana.mostrar_error(ClienteExiste(Exception))
            return 0
        elif not validador.validar_string(nombre):
            self.ventana.mostrar_error(ErrorValidacion("El nombre no puede contener numeros y no puede estar vacio",Exception))
            return 0
        elif not validador.validar_string(apellido) and apellido:
            self.ventana.mostrar_error(ErrorValidacion("El apellido no puede contener numeros",Exception))
            return 0
        elif not validador.telefono(numero):
            self.ventana.mostrar_error(ErrorValidacion("El numero de telefono no es valido, debe empezar con 04..",Exception))
            return 0
        
        #Por ahora no se registra nacionalidad
        try:
            self.tablaClientes.insert(cedula,nombre,apellido,direccion,numero)
            QMessageBox.information(self.ventana,"REGISTRO EXITOSO","Se ha registrado correctamente",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            self.reiniciar_vista_registrar_clientes()
        except Exception as e:
            self.ventana.mostrar_error(ErrorRegistro(e))
            
    def reiniciar_vista_registrar_clientes(self):
        self.ui.line_cedula_rcliente.setText("")
        self.ui.line_nombre_rcliente.setText("")
        self.ui.line_apellido_rcliente.setText("")
        self.ui.combo_nacionalidad_rcliente.setCurrentIndex(0)
        self.ui.text_descripcion_rcliente.setText("")
        self.ui.line_telefono_rcliente.setText("")
        self.ventana.ui.stacked_widget.setCurrentIndex(3)
        

class ClienteExiste(Exception):
    def __init__(self,error):
        super().__init__(f"Cliente YA ha sido Registrado")
        self.e = error
        
class ErrorRegistro(Exception):
    def __init__(self,error):
        super().__init__(f"No se ha podido insertar en la BD")
        self.e = error

class ErrorValidacion(Exception):
    def __init__(self,mensaje,error):
        super().__init__(mensaje)
        self.e = error