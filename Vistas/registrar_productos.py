from conexion_bd.tablas import TablaProductos
from Validacion.validador import Validador
class VistaRegistrarProductos:
    def __init__(self,ventana) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_registrar_rproducto.pressed.connect(self.registrar_producto)
        Validador().solo_texto_productos(self.ui.line_nombre_rproducto)
    
        
    def registrar_producto(self):
        nombre = self.ui.line_nombre_rproducto.text()
        descripcion = self.ui.text_descripcion_rproducto.toPlainText()
        precio = self.ui.double_precio_rproducto.text().replace(",",".")
        
        if nombre == "":
            self.ventana.mostrar_mensaje("No tiene nombre","Dale un nombre al producto")
            return 0
        
        if float(precio)<=0:
            self.ventana.mostrar_mensaje("Precio invalido","El precio debe ser mayor a 0")
            return 0
        
        try:
            tabla = TablaProductos()
            tabla.insert(nombre,descripcion,precio)
            self.ventana.mostrar_mensaje("Producto registrado","El producto se ha registrado correctamente")
            self.ventana.vista_productos.buscar_producto()
            self.reiniciar()
            self.ui.stacked_widget.setCurrentWidget(self.ui.vista_facturar)
        except Exception as e:
            self.ventana.mostrar_error(ErrorRegistro(e))
    
    def reiniciar(self):
        self.ui.line_nombre_rproducto.setText("")
        self.ui.text_descripcion_rproducto.setText("")
        self.ui.double_precio_rproducto.setValue(0.0)

class ErrorRegistro(Exception):
    def __init__(self,error):
        super().__init__(f"No se ha podido insertar en la BD")
        self.e = error