from interfaz_ui.interfaz_principal import Ui_MainWindow
from Vistas.registrar_clientes import VistaRegistrarClientes
from PySide6.QtWidgets import QMainWindow,QApplication,QMessageBox
import sys

class MainWindow(VistaRegistrarClientes,QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        VistaRegistrarClientes.__init__(self,self)
        self.crear_logica()
        self.show()
    
    def crear_logica(self):
        self.ui.stacked_widget.setCurrentIndex(3)
        self.asignar_slots_vistas()
    
    def asignar_slots_vistas(self):
        self.ui.boton_v_registrar.pressed.connect(lambda: self.ui.stacked_widget.setCurrentIndex(0))
        self.ui.boton_v_registrar_clientes.pressed.connect(lambda: self.ui.stacked_widget.setCurrentIndex(1))
        self.ui.boton_v_facturar.pressed.connect(lambda: self.ui.stacked_widget.setCurrentIndex(3))
        self.ui.boton_v_clientes.pressed.connect(lambda: self.ui.stacked_widget.setCurrentIndex(4))
        self.ui.boton_v_productos.pressed.connect(lambda: self.ui.stacked_widget.setCurrentIndex(5))
        self.ui.boton_v_cierre.pressed.connect(lambda: self.ui.stacked_widget.setCurrentIndex(6))
        self.ui.boton_v_configuracion.pressed.connect(lambda: self.ui.stacked_widget.setCurrentIndex(7))
        self.ui.boton_v_cerrar_sesion.pressed.connect(lambda: self.ui.stacked_widget.setCurrentIndex(8))
        self.ui.boton_v_registar_productos.pressed.connect(lambda: self.ui.stacked_widget.setCurrentIndex(9))
    
    def mostrar_error(self,error):
        QMessageBox.warning(self,"Ha ocurrido un error",f"Ha ocurrido el siguiente error: {error}",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
