from interfaz_ui.interfaz_principal import Ui_MainWindow
from Vistas.registrar_clientes import VistaRegistrarClientes
from Vistas.registrar_productos import VistaRegistrarProductos
from Vistas.productos import VistaProductos
from Vistas.facturar import VistaFacturar
from Vistas.cierre import VistaCierre
from Vistas.configuracion import VistaConfiguracion
from PySide6.QtWidgets import QMainWindow,QApplication,QMessageBox
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.vista_registrar_clientes = VistaRegistrarClientes(self)
        self.vista_registrar_productos = VistaRegistrarProductos(self)
        self.vista_productos = VistaProductos(self)
        self.vista_facturar = VistaFacturar(self)
        self.vista_cierre = VistaCierre(self)
        self.vista_configuracion = VistaConfiguracion(self)
        self.crear_logica()
        self.show()
    
    def crear_logica(self):
        self.ui.stacked_widget.setCurrentWidget(self.ui.vista_facturar)
        self.asignar_slots_vistas()
    
    def asignar_slots_vistas(self):
        self.ui.boton_v_registrar_clientes.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.vista_registrar_clientes))
        self.ui.boton_v_facturar.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.vista_facturar))
        self.ui.boton_v_productos.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.vista_productos))
        self.ui.boton_v_cierre.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.vista_cierre))
        self.ui.boton_v_configuracion.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.vista_configuracion))
        self.ui.boton_v_registar_productos.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.vista_registrar_productos))
        # self.ui.boton_v_cerrar_sesion.pressed.connect()
    
    def mostrar_mensaje(self,titulo,mensaje):
        QMessageBox.information(self,titulo,mensaje,QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
    
    def mostrar_error(self,error):
        QMessageBox.warning(self,"Ha ocurrido un error",f"Ha ocurrido el siguiente error: {error}",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
