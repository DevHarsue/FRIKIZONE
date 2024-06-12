from conexion_bd.tablas import TablaClientes,TablaDivisas,TablaMetodos,TablaProductos,TablaRoles,TablaUsuarios,TablaVentas,TablaVentasDetalles,TablaTotalesDiarios
from utilidades.funciones_utiles import obtener_fecha,obtener_tasa_bcv
from utilidades.scrapping_web_cne import BuscadorPersonas
from interfaz_ui.interfaz_principal import Ui_MainWindow
from interfaz_ui.ventana1 import Ui_MainWindow_2
from PySide6.QtWidgets import QMainWindow,QApplication,QMessageBox
from PySide6.QtGui import QIntValidator
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        self.preparar_registro_clientes()
        self.show()
        self.tablaClientes = TablaClientes()
    
    def preparar_registro_clientes(self):
        #Coloco el estado principal de checkbox y le agrego el slot
        self.ventana.EDITAR.setChecked(True)
        self.ventana.EDITAR.clicked.connect(self.cambiar_estado_inputs_nombre)
        
        #Estado inicial de line edits para el nombre
        self.ventana.NOMBRE.setEnabled(False)
        self.ventana.APELLIDO.setEnabled(False)
        
        #se agrega un validador al line edit de cedula para que solo admita numeros
        self.ventana.CEDULA.setValidator(QIntValidator())
        
        #Conectamos los slots de los botones
        self.ventana.BUSCAR.clicked.connect(self.buscar_cliente)
        self.ventana.REGISTRAR.clicked.connect(self.registrar_cliente)
    
    def cambiar_estado_inputs_nombre(self):
        if not self.ventana.EDITAR.isChecked():
            self.ventana.NOMBRE.setEnabled(True)
            self.ventana.APELLIDO.setEnabled(True)
        else:
            self.ventana.NOMBRE.setEnabled(False)
            self.ventana.APELLIDO.setEnabled(False)
    
    def buscar_cliente(self):
        cedula = self.ventana.CEDULA.text()
        if cedula == "":
            QMessageBox.information(self,"Cedula vacia","Porfavor ingresa un numero de cedula",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0
        try:
            persona = self.tablaClientes.select(int(cedula))
            nombre = ""
            if not bool(persona):
                nombre = BuscadorPersonas().buscar_persona(self.ventana.NACIONALIDAD.currentText(),cedula)
            else:
                nombre = persona[0].nombre,persona[0].apellido
        
            self.ventana.NOMBRE.setText(nombre[0])
            self.ventana.APELLIDO.setText(nombre[1])
        except Exception as e:
            print(e)
            self.ventana.EDITAR.setChecked(False)
            self.cambiar_estado_inputs_nombre()

    def registrar_cliente(self):
        cedula = self.ventana.CEDULA.text()
        nombre = self.ventana.NOMBRE.text()
        apellido = self.ventana.APELLIDO.text()
        nacionalidad = self.ventana.NACIONALIDAD.currentText()
        direccion = self.ventana.DIRECCION.toPlainText()
        numero = self.ventana.TELEFONO.text()
        
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
