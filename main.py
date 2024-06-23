from interfaz.interfaz_principal import Ui_MainWindow
from Vistas.registrar_clientes import VistaRegistrarClientes
from Vistas.registrar_productos import VistaRegistrarProductos
from Vistas.productos import VistaProductos
from Vistas.facturar import VistaFacturar
from Vistas.cierre import VistaCierre
from Vistas.configuracion import VistaConfiguracion
from PySide6.QtWidgets import QMainWindow,QApplication,QMessageBox
from interfaz.login.ui_ventana1 import Ui_login
from conexion_bd.tablas import TablaUsuarios
from Validacion.hash import texto_a_hash
import sys


    # Ventana Principal
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
    
    def preguntar(self,titulo,texto):
        return QMessageBox.question(self,titulo,texto,QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,QMessageBox.StandardButton.No)


######################## Codigo de Login ######################## 


# Ventana Login
class VentanaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.slotsbotones()
        self.ventana = False
        self.show()

    # BOTONES
    
    
    def slotsbotones(self):
        self.ui.BotonLogin.pressed.connect(self.iniciar_sesion)


    # Slots

    def iniciar_sesion(self):
        if self.ventana:
            return 0
        nombre = self.ui.Usuario.text()
        contrasena = texto_a_hash(self.ui.Clave.text())
        
        usuario = TablaUsuarios().select(1)[0]
        
        if nombre == usuario.nombre and contrasena==usuario._contraseña:
            self.close()
            self.ventana = MainWindow()
            self.ventana.show()
            
        else:
            self.ui.clave_incorrecta.setText("Clave Incorrecta")
            self.ui.usuario_incorrecto.setText("Usuario Incorrecto")





# Ejecutar Interfaz

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaLogin()
    sys.exit(app.exec())
    
    
    