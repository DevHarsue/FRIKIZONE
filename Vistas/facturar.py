from Validacion.validador import Validador
from conexion_bd.tablas import TablaClientes,TablaDivisas
from PySide6.QtWidgets import QMessageBox,QTableWidgetItem

class VistaFacturar:
    def __init__(self,ventana) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_buscar_cliente_facturar.pressed.connect(self.buscar_paciente)
        self.ui.boton_facturar.pressed.connect(self.facturar)
        self.ui.line_cedula_facturar.textChanged.connect(self.reiniciar_cliente)
        self.ui.boton_buscar_producto_facturar.pressed.connect(self.seleccionar_producto)
        Validador().cedulas(self.ui.line_cedula_facturar)
        self.ui.double_bs_facturar.textChanged.connect(self.calcular)
        self.ui.spin_cop_facturar.textChanged.connect(self.calcular)
        self.ui.double_dolares_facturar.textChanged.connect(self.calcular)
        self.total = 0
    
    def buscar_paciente(self):
        cedula = self.ui.line_cedula_facturar.text()
        if cedula == "" or (len(cedula)<7):
            self.ventana.mostrar_mensaje("Cedula invalidad","Porfavor ingresa un numero de cedula valido")
            return 0
        
        cliente = TablaClientes().select(int(cedula))
        if bool(cliente):
            cliente = cliente[0]
            self.ui.line_nombre_facturar.setText(cliente.nombre)
            self.ui.line_apellido_facturar.setText(cliente.apellido)
        else:
            respuesta = self.ventana.preguntar("Cliente No encontrado","¿Desea registrar cliente?")
            if respuesta == QMessageBox.StandardButton.Yes:
                self.ui.stacked_widget.setCurrentWidget(self.ui.vista_registrar_clientes)
                self.ui.line_cedula_rcliente.setText(cedula)
                self.ui.combo_nacionalidad_rcliente.setCurrentIndex(self.ui.combo_nacionalidad_facturar.currentIndex())
                
            return 0 
        
    def reiniciar_cliente(self):
        self.ui.line_nombre_facturar.setText("")
        self.ui.line_apellido_facturar.setText("")
    
    def seleccionar_producto(self):
        self.ventana.vista_productos.compra = True
        self.ui.stacked_widget.setCurrentWidget(self.ui.vista_productos)
        
        
    def facturar(self):
        if self.ui.line_nombre_facturar.text()=="":
            self.ventana.mostrar_mensaje("Cliente no seleccionado","Porfavor busque un cliente")
            return 0
    
    def meter_producto(self):
        datos = self.ventana.vista_productos.datos
        datos.pop(2)
        datos.append(self.ventana.vista_productos.cantidad)
        datos.append(float(datos[-1])*float(datos[-2]))
        
        self.ui.table_productos_facturar.insertRow(self.ui.table_productos_facturar.rowCount())
        row = self.ui.table_productos_facturar.rowCount()-1
        for i,x in enumerate(datos):
            self.ui.table_productos_facturar.setItem(row,i,QTableWidgetItem(str(x)))
        
        self.ui.table_productos_facturar.setItem(row,i,QTableWidgetItem(str(x)))
        
        self.total+=float(datos[-1]) if datos[-1]!="" else 0
        
        self.ui.label_total.setText("TOTAL EN DOLARES: "+str(self.total))
        self.calcular()
        
    def calcular(self):
        pass
        # tasa_bolivares = float(TablaDivisas().select(1)[0].relacion)
        # tasa_cop = float(TablaDivisas().select(2)[0].relacion)
        # self.ui.label_dolar_facturar("Valor $: "+str(self.total))
        # self.ui.label_bolivar_facturar("Valor BS: "+str(self.total*tasa_bolivares))
        # self.ui.label_cop_facturar("Valor COP: "+str(self.total*tasa_cop))
            
