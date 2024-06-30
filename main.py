from Vistas.registrar_clientes import VistaRegistrarClientes
from Vistas.registrar_productos import VistaRegistrarProductos
from Vistas.productos import VistaProductos
from Vistas.facturar import VistaFacturar
from Vistas.cierre import VistaCierre
from Vistas.actualizar_producto import VistaActualizarProducto
from Vistas.configuracion import VistaConfiguracion
from Vistas.divisas import VistaDivisas
from Vistas.editar_cliente import VistaEditarCliente
from Vistas.data import VistaData
from interfaz.login.ui_ventana1 import Ui_login
from conexion_bd.tablas import TablaUsuarios
from Validacion.hash import texto_a_hash
import sys
from PySide6.QtWidgets import QApplication,QMainWindow
from submain import MainWindow


# Ventana Login
class VentanaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.slotsbotones()
        self.ventana = False
        self.show()

    def slotsbotones(self):
        self.ui.BotonLogin.pressed.connect(self.iniciar_sesion)
        
    def iniciar_sesion(self):
        if self.ventana:
            return 0
        nombre = self.ui.Usuario.text()
        contrasena = texto_a_hash(self.ui.Clave.text())
        
        usuario = TablaUsuarios().select(1)[0]
        
        if nombre == usuario.nombre and contrasena==usuario._contraseña:
            self.close()
            self.ventana = MainWindow(usuario.id)
            self.funcionalidades_main(self.ventana)
            self.ventana.show()
            
        else:
            self.ui.clave_incorrecta.setText("Clave Incorrecta")
            self.ui.usuario_incorrecto.setText("Usuario Incorrecto")

    def funcionalidades_main(self,window):
        window.vista_registrar_clientes = VistaRegistrarClientes(window)
        window.vista_registrar_productos = VistaRegistrarProductos(window)
        window.vista_productos = VistaProductos(window)
        window.vista_facturar = VistaFacturar(window)
        window.vista_cierre = VistaCierre(window)
        window.vista_configuracion = VistaConfiguracion(window)
        window.vista_actualizar_productos = VistaActualizarProducto(window)
        window.vista_divisas = VistaDivisas(window)
        window.vista_editar_clientes = VistaEditarCliente(window)
        window.vista_data = VistaData(window)


# Ejecutar Interfaz
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaLogin()
    sys.exit(app.exec())
    
    
    