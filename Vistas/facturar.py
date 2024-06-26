from Validacion.validador import Validador
from conexion_bd.tablas import TablaClientes,TablaDivisas,TablaVentas,TablaVentasIngresos,TablaVentasProductos
from PySide6.QtWidgets import QTableWidgetItem
from submain import MainWindow
from utilidades.funciones_utiles import obtener_fecha
from PDF.PDFS import FacturaPDF
import os
import webbrowser

class VistaFacturar:
    def __init__(self,ventana: MainWindow) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_buscar_cliente_facturar.pressed.connect(self.buscar_cliente)
        self.ui.boton_facturar.pressed.connect(self.facturar)
        self.ui.line_cedula_facturar.textChanged.connect(self.reiniciar_cliente)
        self.ui.boton_buscar_producto_facturar.pressed.connect(self.seleccionar_producto)
        Validador().cedulas(self.ui.line_cedula_facturar)
        self.total = 0
        self.ui.label_bs.mousePressEvent = self.cargar_bs
        self.ui.label_dolar.mousePressEvent = self.cargar_dolar
        self.ui.label_cop.mousePressEvent = self.cargar_cop
        self.ui.double_bs_facturar.valueChanged.connect(self.calcular_bs)
        self.ui.double_dolares_facturar.valueChanged.connect(self.calcular_dolar)
        self.ui.spin_cop_facturar.valueChanged.connect(self.calcular_cop)
        self.tasa_bolivares = float(TablaDivisas().select(1)[0].relacion)
        self.tasa_cop = float(TablaDivisas().select(2)[0].relacion)
        self.ui.boton_facturar.setDisabled(True)
        self.ui.table_productos_facturar.itemActivated.connect(self.borrar_producto)
        self.ui.table_productos_facturar.itemPressed.connect(self.borrar_producto)
        
    
    def buscar_cliente(self):
        cedula = self.ui.line_cedula_facturar.text()
        if cedula == "" or (len(cedula)<7):
            self.ventana.mostrar_mensaje("Cedula invalidad","Porfavor ingresa un numero de cedula valido")
            return 0
        
        self.cliente = TablaClientes().select(int(cedula))
        if bool(self.cliente):
            self.cliente = self.cliente[0]
            self.ui.line_nombre_facturar.setText(self.cliente.nombre)
            self.ui.line_apellido_facturar.setText(self.cliente.apellido)
        else:
            self.cliente = False
            self.ventana.preguntar("Cliente No encontrado","¿Desea registrar cliente?")
            respuesta = self.ventana.respuesta
            if respuesta == True:
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
        productos = []
        imprimir = []
        for x in range(self.ui.table_productos_facturar.rowCount()):
            id = self.ui.table_productos_facturar.item(x,0).text()
            nombre = self.ui.table_productos_facturar.item(x,1).text()
            precio = self.ui.table_productos_facturar.item(x,2).text()
            cantidad = self.ui.table_productos_facturar.item(x,3).text()
            subtotal = self.ui.table_productos_facturar.item(x,4).text()
            productos.append((id,cantidad))
            imprimir.append({'numero': id, 'articulo': nombre,'qty': cantidad, 'precio': precio,"subtotal":subtotal},)
            
        tabla = TablaVentas()
        tabla.insert(obtener_fecha(),self.ventana.usuario_id,self.cliente.id)
        venta = tabla.select_ultima_venta()[0]
        
        tabla = TablaVentasIngresos()
        tabla.insert(venta.id,1,self.ui.double_bs_facturar.value())
        tabla.insert(venta.id,2,self.ui.spin_cop_facturar.value())
        tabla.insert(venta.id,3,self.ui.double_dolares_facturar.value())
        
        tabla = TablaVentasProductos()
        for producto in productos:
            tabla.insert(venta.id,producto[0],producto[1])
        self.ventana.mostrar_mensaje("Venta Realizada","Venta Realizada Correctamente")
        
        pdf = FacturaPDF(venta.id,obtener_fecha(),f"{self.cliente.nombre} {self.cliente.apellido}",self.cliente.telefono,self.cliente.direccion,imprimir,self.total,self.ui.double_dolares_facturar.value(),self.ui.double_bs_facturar.value(),self.ui.spin_cop_facturar.value())
        documentos_path = str(os.path.expanduser("~\\Documents"))
        try:
            os.makedirs(documentos_path+"\\FRIKIZONE")
        except FileExistsError:
            pass
        path = f"{documentos_path}\\FRIKIZONE\\factura_{venta.id}_{self.cliente.nombre}.pdf"
        pdf.output(path)
        webbrowser.open_new(path)
        
        self.reiniciar_cliente()
        self.reiniciar_productos()
    
    def meter_producto(self):
        datos = self.ventana.vista_productos.datos
        datos.pop(2)
        datos.append(self.ventana.vista_productos.cantidad)
        datos.append(float(datos[-1])*float(datos[-2]))
        
        for x in range(self.ui.table_productos_facturar.rowCount()):
            if self.ui.table_productos_facturar.item(x,0).text() == datos[0]:
                cantidad = int(self.ui.table_productos_facturar.item(x,3).text())+self.ventana.vista_productos.cantidad
                self.ui.table_productos_facturar.setItem(x,3,QTableWidgetItem(str(cantidad)))
                self.ui.table_productos_facturar.setItem(x,4,QTableWidgetItem(str(cantidad*float(datos[-3]))))
                self.calcular()
                return 0
        
        self.ui.table_productos_facturar.insertRow(self.ui.table_productos_facturar.rowCount())
        row = self.ui.table_productos_facturar.rowCount()-1
        for i,x in enumerate(datos):
            self.ui.table_productos_facturar.setItem(row,i,QTableWidgetItem(str(x)))
        
        self.calcular()
        self.calcular_bs()
        self.calcular_dolar()
        self.calcular_cop()
        
    def calcular(self):
        row = self.ui.table_productos_facturar.rowCount()
        self.total = 0
        for x in range(row):
            self.total +=float(self.ui.table_productos_facturar.item(x,4).text())
        
        self.ui.label_total.setText("TOTAL EN DOLARES: "+str(self.total))
        self.ui.label_dolar.setText(str(self.total))
        self.ui.label_bs.setText(str(self.total*self.tasa_bolivares))
        self.ui.label_cop.setText(str(int(self.total*self.tasa_cop)))
        
    
    def cargar_bs(self,e):
        self.ui.double_bs_facturar.setValue(self.total*self.tasa_bolivares)
    def cargar_dolar(self,e):
        self.ui.double_dolares_facturar.setValue(self.total)
    def cargar_cop(self,e):
        self.ui.spin_cop_facturar.setValue(self.total*self.tasa_cop)
    
    def calcular_dolar(self):
        ingresado_bs = self.ui.double_bs_facturar.value()
        ingresado_cop = self.ui.spin_cop_facturar.value()
        dolar = self.total-((ingresado_bs/self.tasa_bolivares)+ingresado_cop/self.tasa_cop)
        ingresado_dolar = self.ui.double_dolares_facturar.value()
        if ingresado_dolar > dolar:
            self.ui.double_dolares_facturar.setValue(dolar)
            ingresado_dolar = dolar
            
        restante_dolar =round(dolar-ingresado_dolar,2)
        self.ui.label_dolar.setText(str(round(restante_dolar,2)))
        self.ui.label_bs.setText(str(round(restante_dolar*self.tasa_bolivares,2)))
        self.ui.label_cop.setText(str(round(restante_dolar*self.tasa_cop,-2)))
        self.comprobar_factura()
        
        
    def calcular_bs(self):
        ingresado_dolar = self.ui.double_dolares_facturar.value()
        ingresado_cop = self.ui.spin_cop_facturar.value()
        bs = round(self.total-(ingresado_dolar+ingresado_cop/self.tasa_cop),2)*self.tasa_bolivares
        ingresado_bs = self.ui.double_bs_facturar.value()
        if ingresado_bs > bs:
            self.ui.double_bs_facturar.setValue(bs)
            ingresado_bs = bs
            
        restante_bs = bs-ingresado_bs
        self.ui.label_bs.setText(str(round(restante_bs,2)))
        self.ui.label_dolar.setText(str(round(restante_bs/self.tasa_bolivares,2)))
        self.ui.label_cop.setText(str(round((restante_bs/self.tasa_bolivares)*self.tasa_cop,-2)))
        self.comprobar_factura()

    def calcular_cop(self):
        ingresado_bs = self.ui.double_bs_facturar.value()
        ingresado_dolar = self.ui.double_dolares_facturar.value()
        cop = round((self.total-(ingresado_dolar+ingresado_bs/self.tasa_bolivares))*self.tasa_cop,-2)
        ingresado_cop = self.ui.spin_cop_facturar.value()
        if ingresado_cop > cop:
            self.ui.spin_cop_facturar.setValue(cop)
            ingresado_cop = cop
            
        restante_cop = cop-ingresado_cop
        self.ui.label_cop.setText(str(round(restante_cop,2)))
        self.ui.label_dolar.setText(str(round(restante_cop/self.tasa_cop,2)))
        self.ui.label_bs.setText(str(round((restante_cop/self.tasa_cop)*self.tasa_bolivares,2)))
        self.comprobar_factura()
    
    def comprobar_factura(self):
        dolar = float(self.ui.label_dolar.text())
        bs = float(self.ui.label_bs.text())
        cop = float(self.ui.label_cop.text())

        if dolar==0 and bs==0 and cop==0 and self.ui.table_productos_facturar.rowCount>0:
            self.ui.boton_facturar.setEnabled(True)
        else:
            self.ui.boton_facturar.setDisabled(True)
            
    def reiniciar_productos(self):
        while self.ui.table_productos_facturar.rowCount() > 0:
            self.ui.table_productos_facturar.removeRow(0)
        self.calcular()
        self.calcular_bs()
        self.calcular_cop()
        self.calcular_dolar()
    
    def borrar_producto(self):
        row = self.ui.table_productos_facturar.currentRow()
        self.ventana.preguntar("Quitar Producto","¿Quitar Producto de la Venta?")
        respuesta = self.ventana.respuesta
        if not respuesta:
            return 0
        self.ui.table_productos_facturar.removeRow(row)
        self.comprobar_factura
        self.calcular()
        self.calcular_bs()
        self.calcular_cop()
        self.calcular_dolar()