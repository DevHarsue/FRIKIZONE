

class VistaRegistrarProductos:
    def __init__(self,ventana) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_registrar_rproducto.pressed.connect(self.registrar_producto)
        
    def registrar_producto(self):
        nombre = self.ui.