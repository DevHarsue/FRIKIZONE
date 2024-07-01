from submain import MainWindow
from ventanas import VentanaConfiguracion,VentanaRegistro
class VistaConfiguracion:
    def __init__(self,ventana: MainWindow) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_configurar_bd.pressed.connect(self.configuracion)
        self.ui.boton_registrar_usuarios.pressed.connect(self.registro)
        
    def configuracion(self):
        self.ventana.close()
        self.config = VentanaConfiguracion(self.ventana)
        self.config.show()
        self.config.ui.boton_volver.setEnabled(True)
    
    def registro(self):
        self.ventana.close()
        self.register = VentanaRegistro(self.ventana)
        self.register.show()
        self.register.ui.boton_volver.setEnabled(True)
        self.register.ui.comboBox.removeItem(0)