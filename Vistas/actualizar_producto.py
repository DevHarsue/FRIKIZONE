from submain import MainWindow
from conexion_bd.tablas import TablaProductos,TablaVentasProductos

class VistaActualizarProducto:
    def __init__(self,ventana: MainWindow) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_volver_aproducto.pressed.connect(self.volver)
        self.ui.boton_actualizar_aproducto.pressed.connect(self.actualizar)
        self.ui.boton_borrar_aproducto.pressed.connect(self.borrar)
    
    def cargar_producto(self):
        self.datos = self.ventana.vista_productos.datos
        self.ui.line_nombre_aproducto.setText(self.datos[1])
        self.ui.text_descripcion_aproducto.setText(self.datos[2])
        self.ui.double_precio_aproducto.setValue(float(self.datos[3]))
    
    def actualizar(self):
        nombre = self.ui.line_nombre_aproducto.text()
        descripcion = self.ui.text_descripcion_aproducto.toPlainText()
        precio = self.ui.double_precio_aproducto.value()
        if nombre=="":
            self.ventana.mostrar_mensaje("Sin Nombre","El nombre del producto no puede estar vacio")
            return 0
        if precio<=0:
            self.ventana.mostrar_mensaje("Sin Precio","El precio del producto no puede ser 0")
            return 0

        TablaProductos().update(self.datos[0],{"producto_nombre":nombre,"producto_descripcion":descripcion,"producto_valor":precio})
        self.ventana.mostrar_mensaje("Actualizacion Completada","Producto Actualizado")
        for x in range(self.ui.table_productos_facturar.rowCount()):
            if self.ui.table_productos_facturar.item(x,0).text() == str(self.datos[0]):
                self.ui.table_productos_facturar.item(x,1).setText(nombre)
                self.ui.table_productos_facturar.item(x,2).setText(str(precio))
                self.ui.table_productos_facturar.item(x,4).setText(str(precio*int(self.ui.table_productos_facturar.item(x,3).text())))
                self.ventana.vista_facturar.calcular()
                self.ventana.vista_facturar.calcular_bs()
                self.ventana.vista_facturar.calcular_cop()
                self.ventana.vista_facturar.calcular_dolar()
                
        self.volver()

    
    def borrar(self):
        self.ventana.preguntar("Borrar Producto","Se borrara todo lo relacionado a este producto\n¿Estas seguro de borrar?")
        if not self.ventana.respuesta:
            return 0
        
        TablaVentasProductos().delete_por_producto(self.datos[0])
        TablaProductos().delete(self.datos[0])
        self.ventana.mostrar_mensaje("Producto Borrado","Producto borrado exitosamente")
        for x in range(self.ui.table_productos_facturar.rowCount()):
            if self.ui.table_productos_facturar.item(x,0).text() == str(self.datos[0]):
                self.ui.table_productos_facturar.removeRow(x)
                self.ventana.vista_facturar.calcular()
                self.ventana.vista_facturar.calcular_bs()
                self.ventana.vista_facturar.calcular_cop()
                self.ventana.vista_facturar.calcular_dolar()
        self.volver()
    
    def volver(self):
        self.ui.stacked_widget.setCurrentWidget(self.ui.vista_productos)
        self.ventana.vista_productos.buscar_producto()
        self.ui.line_nombre_aproducto.setText("")
        self.ui.text_descripcion_aproducto.setText("")
        self.ui.double_precio_aproducto.setValue(0)