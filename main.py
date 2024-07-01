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
from Vistas.editar_usuarios import VistaEditarUsuarios
from interfaz.login.ui_ventana1 import Ui_login
from conexion_bd.tablas import TablaUsuarios
from Validacion.hash import texto_a_hash,texto_a_hash_salt
from Validacion.validador import Validador
import sys
from PySide6.QtWidgets import QApplication,QMainWindow
from submain import MainWindow
from conexion_bd.creador_bd_frikizone import CrearEnv
from ventanas import VentanaConfiguracion,VentanaRegistro

# Ventana Login
class VentanaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.slotsbotones()
        self.ventana = False
        self.show()
        self.env = CrearEnv()
        if not self.env.status:
            self.configuracion = VentanaConfiguracion(self)
            self.configuracion.show()
            self.close()
        else:
            self.buscar_usuarios()
        Validador().usuarios(self.ui.Usuario)
        

    def slotsbotones(self):
        self.ui.BotonLogin.pressed.connect(self.iniciar_sesion)
        
    def iniciar_sesion(self):
        if self.ventana:
            return 0
        nombre = texto_a_hash(self.ui.Usuario.text().upper())
        contrasena = texto_a_hash(self.ui.Clave.text())
        
        usuario = TablaUsuarios().select_usuario(nombre)
        
        if not bool(usuario):
            self.ui.usuario_incorrecto.setText("Usuario Incorrecto")
            self.ui.clave_incorrecta.setText("")
            return 0
        else:
            usuario = usuario[0]
            self.ui.usuario_incorrecto.setText("")
        
        if contrasena==usuario._contraseña:
            self.close()
            self.ventana = MainWindow(self,usuario.usuario_rol)
            self.funcionalidades_main(self.ventana)
            self.ventana.show()
            self.ui.Usuario.setText("")
            self.ui.Clave.setText("")
            self.ui.usuario_incorrecto.setText("")
            self.ui.clave_incorrecta.setText("")
        else:
            self.ui.clave_incorrecta.setText("Clave Incorrecta")

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
        window.vista_editar_usuarios = VistaEditarUsuarios(window)
    
    def buscar_usuarios(self):
        usuarios = TablaUsuarios().select_rol(texto_a_hash_salt("SUPERADMIN")) 
        if not bool(usuarios):
            self.registro = VentanaRegistro(self)
            self.registro.show()
            self.close()
        
        


# Ejecutar Interfaz
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaLogin()
    sys.exit(app.exec())
    
    
    