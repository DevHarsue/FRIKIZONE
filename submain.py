from PySide6.QtWidgets import QMainWindow,QDialog
from PySide6.QtCore import Signal
from interfaz.interfaz_principal import Ui_MainWindow
from interfaz.message import Ui_Message
from interfaz.question import Ui_Question

# Ventana Principal
class MainWindow(QMainWindow):
    def __init__(self,usuario_id):
        QMainWindow.__init__(self)
        self.usuario_id = usuario_id
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.crear_logica()
        self.show()
        self.mensaje = Mensaje()
        self.pregunta = Preguntar()
        self.pregunta.respuesta.connect(self.responder)
        self.respuesta = False
    
    def crear_logica(self):
        self.ui.stacked_widget.setCurrentWidget(self.ui.vista_facturar)
        self.asignar_slots_vistas()
    
    def asignar_slots_vistas(self):
        self.ui.boton_v_registrar_clientes.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.vista_registrar_clientes))
        self.ui.boton_v_facturar.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.vista_facturar))
        self.ui.boton_v_productos.pressed.connect(self.cambiar_vista_producto)
        self.ui.boton_v_cierre.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.vista_cierre))
        self.ui.boton_v_configuracion.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.vista_configuracion))
        self.ui.boton_v_registar_productos.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.vista_registrar_productos))
        self.ui.boton_v_divisas.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.vista_divisas))
        # self.ui.boton_v_cerrar_sesion.pressed.connect()
    
    def cambiar_vista_producto(self):
        self.ui.stacked_widget.setCurrentWidget(self.ui.vista_productos)
        self.vista_productos.compra = False
    
    def mostrar_mensaje(self,titulo,mensaje):
        self.mensaje.mostrar(titulo,mensaje)
    def mostrar_error(self,error):
        self.mensaje.mostrar("Error",f"Ha ocurrido el siguiente error:\n{error}")
    def preguntar(self,titulo,texto):
        self.pregunta.mostrar(titulo,texto)

    def responder(self,respuesta):
        if not respuesta:
            self.respuesta=False
        else:
            self.respuesta=True

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