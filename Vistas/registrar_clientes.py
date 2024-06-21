from Hilos.cne import HiloCNE
from conexion_bd.tablas import TablaClientes
from Validacion.validador import Validador
from PySide6.QtWidgets import QMessageBox
from Validacion.validador import Validador

class VistaRegistrarClientes:
    def __init__(self,ventana) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.vista_registrar_clientes()
    
    #Vista Registro Clientes
    def vista_registrar_clientes(self):
        self.tablaClientes = TablaClientes()
        #Coloco el estado principal de checkbox y le agrego el slot
        self.ui.check_editar_rcliente.stateChanged.connect(self.cambiar_estado_line_nombres)
        self.ui.check_editar_rcliente.setChecked(True)
        
        #se agrega un validador al line edit de cedula para que solo admita numeros
        Validador().cedulas(self.ui.line_cedula_rcliente)
        Validador().solo_texto(self.ui.line_nombre_rcliente)
        Validador().solo_texto(self.ui.line_apellido_rcliente)
        Validador().numero_telefono(self.ui.line_telefono_rcliente)
        
        #Conectamos los slots de los botones
        self.ui.boton_buscar_rcliente.clicked.connect(self.buscar_cliente_registro)
        self.ui.boton_registrar_rcliente.clicked.connect(self.registrar_cliente)
    
    def cambiar_estado_line_nombres(self):
        estado = not self.ui.check_editar_rcliente.isChecked()
        self.ui.line_nombre_rcliente.setEnabled(True if estado else False)
        self.ui.line_apellido_rcliente.setEnabled(True if estado else False)
    
    def buscar_cliente_registro(self):
        cedula = self.ui.line_cedula_rcliente.text()
        if cedula == "" or (len(cedula)<7):
            self.ventana.mostrar_mensaje("Cedula invalidad","Porfavor ingresa un numero de cedula valido")
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
            self.ventana.mostrar_mensaje("Cliente ya registrado",f"El cliente ya ha sido registrado antes.")
            
        
    def mostrar_cliente_cne(self,nombre_persona):
        self.ui.line_nombre_rcliente.setText(nombre_persona[0])
        self.ui.line_apellido_rcliente.setText(nombre_persona[1])
    
    def definir_estado(self):
        if self.ui.line_nombre_rcliente.text() == "Cargando del CNE...":
            self.ui.line_apellido_rcliente.setText("")
            self.ui.line_nombre_rcliente.setText("")
            
    def registrar_cliente(self):
        cedula = self.ui.line_cedula_rcliente.text()
        nombre = self.ui.line_nombre_rcliente.text()
        apellido = self.ui.line_apellido_rcliente.text()
        nacionalidad = self.ui.combo_nacionalidad_rcliente.currentText()
        direccion = self.ui.text_descripcion_rcliente.toPlainText()
        numero = self.ui.line_telefono_rcliente.text()
        
        persona = self.tablaClientes.select(int(cedula))
        if bool(persona):
            self.ventana.mostrar_mensaje("Cliente ya registrado","El cliente ya ha sido registrado antes")
            return 0
        if nombre=="":
            self.ventana.mostrar_mensaje("Dato Vacio","El nombre no puede estar vacio")
            return 0
        if apellido=="":
            self.ventana.mostrar_mensaje("Dato Vacio","El apellido no puede estar vacio")
            return 0
        if numero=="" or (len(numero)<10):
            self.ventana.mostrar_mensaje("Telefono invalido","El telefono debe tener al menos 10 digitos")
            return 0
        
        try:
            self.tablaClientes.insert(cedula,nacionalidad,nombre,apellido,direccion,numero)
            self.ventana.mostrar_mensaje("REGISTRO EXITOSO","Se ha registrado correctamente")
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
        self.ventana.ui.stacked_widget.setCurrentWidget(self.ui.vista_facturar)
        
class ErrorRegistro(Exception):
    def __init__(self,error):
        super().__init__(f"No se ha podido insertar en la BD")
        self.e = error