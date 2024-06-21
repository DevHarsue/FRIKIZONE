import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from interfaz.login.ui_ventana1 import Ui_MainWindow
from interfaz.login.ui_ventana4 import Ui_MainWindow as w2
from interfaz.interfaz_principal import Ui_MainWindow as w

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.slotsbotones()

    # BOTONES   
    def slotsbotones(self):
        self.ui.BotonLogin.pressed.connect(self.iniciar_sesion)
        self.ui.BotonRegistro.pressed.connect(self.registrarse)


    # Slots
    def iniciar_sesion(self):    
        self.hide()
        self.ventana = Ventana_principal()
        self.ventana.show()

    def registrarse(self):
        self.hide()
        self.ventana2 = Ventana_registro()
        self.ventana2.show


    # VENTANAS
class Ventana_principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = w()
        self.ventana.setupUi(self)

class Ventana_registro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = w2()
        self.ventana.setupUi(self)


#PARA EJECUTAR
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec())


