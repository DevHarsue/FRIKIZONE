from submain import MainWindow
from conexion_bd.tablas import TablaClientes,TablaVentas,TablaVentasIngresos,TablaVentasProductos
from Validacion.validador import Validador

class VistaEditarCliente:
    def __init__(self, ventana: MainWindow):
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.line_cedula_ecliente.textChanged.connect(self.reiniciar)
        self.ui.combo_nacionalidad_ecliente.currentIndexChanged.connect(self.reiniciar)
        self.ui.boton_buscar_ecliente.pressed.connect(self.buscar_cliente)
        self.ui.boton_actualizar_ecliente.pressed.connect(self.actualizar)
        self.ui.boton_borrar_ecliente.pressed.connect(self.borrar)
        self.tabla = TablaClientes()
        Validador().cedulas(self.ui.line_cedula_ecliente)
        Validador().solo_texto(self.ui.line_nombre_ecliente)
        Validador().solo_texto(self.ui.line_apellido_ecliente)
        Validador().numero_telefono(self.ui.line_telefono_ecliente)
    
    def buscar_cliente(self):
        cedula = self.ui.line_cedula_ecliente.text()
        nacionalidad = self.ui.combo_nacionalidad_ecliente.currentText()
        if cedula == '' or len(cedula)<7:
            self.ventana.mostrar_mensaje("Cedula Invalida","Ingrese una cedula valida")
            return 0
        self.cliente = self.tabla.select_cedula(nacionalidad,cedula)
        if not bool(self.cliente):
            self.ventana.mostrar_mensaje("Cliente no encontrado","El Cliente no ha sido encontrado")
            return 0
        self.cliente = self.cliente[0]
        self.ui.line_nombre_ecliente.setText(self.cliente.nombre)
        self.ui.line_apellido_ecliente.setText(self.cliente.apellido)
        self.ui.text_descripcion_ecliente.setText(self.cliente.direccion)
        self.ui.line_telefono_ecliente.setText(self.cliente.telefono)
        self.ui.line_nombre_ecliente.setDisabled(False)
        self.ui.line_apellido_ecliente.setDisabled(False)
        self.ui.text_descripcion_ecliente.setDisabled(False)
        self.ui.line_telefono_ecliente.setDisabled(False)
        self.ui.boton_actualizar_ecliente.setDisabled(False)
        self.ui.boton_borrar_ecliente.setDisabled(False)
        
        
    def reiniciar(self):
        self.ui.line_nombre_ecliente.setText("")
        self.ui.line_apellido_ecliente.setText("")
        self.ui.text_descripcion_ecliente.setText("")
        self.ui.line_telefono_ecliente.setText("")
        self.ui.line_nombre_ecliente.setDisabled(True)
        self.ui.line_apellido_ecliente.setDisabled(True)
        self.ui.text_descripcion_ecliente.setDisabled(True)
        self.ui.line_telefono_ecliente.setDisabled(True)
        self.ui.boton_actualizar_ecliente.setDisabled(True)
        self.ui.boton_borrar_ecliente.setDisabled(True)
    
    def actualizar(self):
        nombre = self.ui.line_nombre_ecliente.text()
        apellido = self.ui.line_apellido_ecliente.text()
        direccion = self.ui.text_descripcion_ecliente.toPlainText()
        telefono = self.ui.line_telefono_ecliente.text()
        if nombre=="":
            self.ventana.mostrar_mensaje("Dato Vacio","El nombre no puede estar vacio")
            return 0
        if apellido=="":
            self.ventana.mostrar_mensaje("Dato Vacio","El apellido no puede estar vacio")
            return 0
        if telefono=="" or (len(telefono)<10):
            self.ventana.mostrar_mensaje("Telefono invalido","El telefono debe tener al menos 10 digitos")
            return 0
        
        self.tabla.update(self.cliente.id,{"cliente_nombre":nombre,"cliente_apellido":apellido,"cliente_telefono":telefono,"cliente_direccion":direccion})
        
        self.ventana.mostrar_mensaje("Cliente Actualizado","Cliente Actualizado Correctamente")
        self.reiniciar()
        self.ventana.vista_facturar.reiniciar_cliente()
        
    def borrar(self):
        self.ventana.preguntar("Eliminar Cliente","Se eleminaran todos los datos asociados al cliente \n¿Estas seguro de borrar?")
        if not self.ventana.respuesta:
            return 0
        
        tabla_ventas =TablaVentas()
        ventas = tabla_ventas.select_cliente(self.cliente.id)
        if bool(ventas):
            tabla_ingresos = TablaVentasIngresos()
            tabla_productos = TablaVentasProductos()
            for venta in ventas:
                tabla_ingresos.delete_venta(venta.id)
                tabla_productos.delete_venta(venta.id)
                tabla_ventas.delete(venta.id)
        self.tabla.delete(self.cliente.id)
        self.ventana.mostrar_mensaje("Cliente Borrado","Cliente borrado exitosamente")
        self.reiniciar()
        self.ventana.vista_facturar.reiniciar_cliente()
        