from conexion_bd.tablas import *
from interfaz_ui.interfaz_principal import Ui_MainWindow
from utilidades.scrapping_web_cne import BuscadorPersonas
from PySide6.QtWidgets import QMainWindow,QApplication,QMessageBox
from PySide6.QtGui import QIntValidator
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        self.crear_logica()
        self.show()
    
    def crear_logica(self):
        self.ventana.stacked_widget.setCurrentIndex(3)
        self.asignar_slots_vistas()
        self.preparar_registro_clientes()
    
    def asignar_slots_vistas(self):
        self.ventana.boton_v_registrar.pressed.connect(lambda: self.ventana.stacked_widget.setCurrentIndex(0))
        self.ventana.boton_v_registrar_clientes.pressed.connect(lambda: self.ventana.stacked_widget.setCurrentIndex(1))
        self.ventana.boton_v_facturar.pressed.connect(lambda: self.ventana.stacked_widget.setCurrentIndex(3))
        self.ventana.boton_v_clientes.pressed.connect(lambda: self.ventana.stacked_widget.setCurrentIndex(4))
        self.ventana.boton_v_productos.pressed.connect(lambda: self.ventana.stacked_widget.setCurrentIndex(5))
        self.ventana.boton_v_cierre.pressed.connect(lambda: self.ventana.stacked_widget.setCurrentIndex(6))
        self.ventana.boton_v_configuracion.pressed.connect(lambda: self.ventana.stacked_widget.setCurrentIndex(7))
        self.ventana.boton_v_cerrar_sesion.pressed.connect(lambda: self.ventana.stacked_widget.setCurrentIndex(8))
        self.ventana.boton_v_registar_productos.pressed.connect(lambda: self.ventana.stacked_widget.setCurrentIndex(9))
    
    def preparar_registro_clientes(self):
        self.tablaClientes = TablaClientes()
        #Coloco el estado principal de checkbox y le agrego el slot
        self.ventana.check_editar_rcliente.setChecked(True)
        self.ventana.check_editar_rcliente.clicked.connect(self.cambiar_estado_inputs_nombre)
        
        #Estado inicial de line edits para el nombre
        self.ventana.line_nombre_rcliente.setEnabled(False)
        self.ventana.line_apellido_rcliente.setEnabled(False)
        
        #se agrega un validador al line edit de cedula para que solo admita numeros
        self.ventana.line_cedula_rcliente.setValidator(QIntValidator())
        
        #Conectamos los slots de los botones
        self.ventana.boton_buscar_rcliente.clicked.connect(self.buscar_cliente)
        self.ventana.boton_registrar_rcliente.clicked.connect(self.registrar_cliente)
    
    def cambiar_estado_inputs_nombre(self):
        if not self.ventana.check_editar_rcliente.isChecked():
            self.ventana.line_nombre_rcliente.setEnabled(True)
            self.ventana.line_apellido_rcliente.setEnabled(True)
        else:
            self.ventana.line_nombre_rcliente.setEnabled(False)
            self.ventana.line_apellido_rcliente.setEnabled(False)
    
    def buscar_cliente(self):
        cedula = self.ventana.line_cedula_rcliente.text()
        if cedula == "":
            QMessageBox.information(self,"Cedula vacia","Porfavor ingresa un numero de cedula",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0
        try:
            persona = self.tablaClientes.select(int(cedula))
            nombre = ""
            if not bool(persona):
                nombre = BuscadorPersonas().buscar_persona(self.ventana.combo_nacionalidad_rcliente.currentText(),cedula)
            else:
                nombre = persona[0].nombre,persona[0].apellido
        
            self.ventana.line_nombre_rcliente.setText(nombre[0])
            self.ventana.line_apellido_rcliente.setText(nombre[1])
        except Exception as e:
            print(e)
            self.ventana.check_editar_rcliente.setChecked(False)
            self.cambiar_estado_inputs_nombre()

    def registrar_cliente(self):
        cedula = self.ventana.line_cedula_rcliente.text()
        nombre = self.ventana.line_nombre_rcliente.text()
        apellido = self.ventana.line_apellido_rcliente.text()
        nacionalidad = self.ventana.combo_nacionalidad_rcliente.currentText()
        direccion = self.ventana.text_descripcion_rcliente.toPlainText()
        numero = self.ventana.line_telefono_rcliente.text()
        
        #Aqui deberian ir las validaciones
        
        #Por ahora no se registra nacionalidad
        try:
            self.tablaClientes.insert(cedula,nombre,apellido,direccion,numero)
            QMessageBox.information(self,"REGISTRO EXITOSO","Se ha registrado correctamente",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
        except Exception as e:
            print(e)
            QMessageBox.error(self,"Ha ocurrido un error","Intenta de nuevo, si el problema persiste, contacte con el proveedor",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
