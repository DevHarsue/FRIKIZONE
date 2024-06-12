from conexion_bd.tablas import TablaClientes,TablaDivisas,TablaMetodos,TablaProductos,TablaRoles,TablaUsuarios,TablaVentas,TablaVentasDetalles,TablaTotalesDiarios
from utilidades.funciones_utiles import obtener_fecha,obtener_tasa_bcv
from utilidades.scrapping_web_cne import BuscadorPersonas
from interfaz_ui.interfaz_principal import Ui_MainWindow
from interfaz_ui.ventana1 import Ui_MainWindow_2
from PySide6.QtWidgets import QMainWindow,QApplication
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        self.show()
        self.ventana.pushButton.clicked.connect(self.cambiar_ventana)
    
    def cambiar_ventana(self):
        self.ventana_2 = Ui_MainWindow_2()
        self.ventana_2.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
