from PySide6.QtWidgets import QMainWindow
from interfaz.interfaz_principal import Ui_MainWindow
from Validacion.hash import texto_a_hash_salt

from ventanas import Mensaje,Preguntar

# Ventana Principal
class MainWindow(QMainWindow):
    def __init__(self,login,rol):
        QMainWindow.__init__(self)
        self.rol = rol
        self.login = login
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
        self.ui.boton_v_editar_clientes.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.vista_editar_clientes))
        self.ui.boton_v_data.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.vista_data))
        self.ui.boton_v_cerrar_sesion.pressed.connect(self.cerrar)
        self.ui.boton_v_cambiar_usuarios.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.vista_editar_usuarios))
        self.ajustar()
    
    def ajustar(self):
        if self.rol == texto_a_hash_salt("USER"):
            self.ui.boton_v_registar_productos.hide()
            self.ui.boton_v_editar_clientes.hide()
            self.ui.boton_v_data.hide()
            self.ui.boton_v_configuracion.hide()
            self.ui.boton_rehacer_cierre.hide()
        elif self.rol == texto_a_hash_salt("ADMIN"):
            self.ui.boton_configurar_bd.hide()
    
    def cerrar(self):
        self.login.show()
        self.login.ventana = False
        self.close()
    
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
