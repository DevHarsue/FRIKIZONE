from Validacion.validador import Validador
from conexion_bd.tablas import TablaClientes,TablaDivisas
from PySide6.QtWidgets import QMessageBox,QTableWidgetItem
from submain import MainWindow

class VistaFacturar:
    def __init__(self,ventana: MainWindow) -> None:
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
        self.ui.label_bs.mousePressEvent = self.cargar_bs
        self.ui.label_dolar.mousePressEvent = self.cargar_dolar
        self.ui.label_cop.mousePressEvent = self.cargar_cop
        self.ui.double_bs_facturar.valueChanged.connect(self.calcular_restante)
        self.ui.double_dolares_facturar.valueChanged.connect(self.calcular_restante)
        self.ui.spin_cop_facturar.valueChanged.connect(self.calcular_restante)
        self.tasa_bolivares = float(TablaDivisas().select(1)[0].relacion)
        self.tasa_cop = float(TablaDivisas().select(2)[0].relacion)
        
    
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
        self.calcular_restante()
        
    def calcular(self):
        row = self.ui.table_productos_facturar.rowCount()
        total = 0
        for x in range(row):
            total +=float(self.ui.table_productos_facturar.item(x,4).text())
        
        self.ui.label_total.setText("TOTAL EN DOLARES: "+str(total))
        self.ui.label_dolar.setText(str(total))
        self.ui.label_bs.setText(str(total*self.tasa_bolivares))
        self.ui.label_cop.setText(str(int(total*self.tasa_cop)))
    
    def cargar_bs(self,e):
        valor = self.ui.label_bs.text()
        self.ui.double_bs_facturar.setValue(float(valor))
    def cargar_dolar(self,e):
        valor = self.ui.label_dolar.text()
        self.ui.double_dolares_facturar.setValue(float(valor))
    def cargar_cop(self,e):
        valor = self.ui.label_cop.text()
        self.ui.spin_cop_facturar.setValue(float(valor))
    
    def calcular_restante(self):
        bs = float(self.ui.label_bs.text())
        dolar = float(self.ui.label_dolar.text())
        cop = int(self.ui.label_cop.text())
        
        ingresado_bs = self.ui.double_bs_facturar.value()
        ingresado_dolar = self.ui.double_dolares_facturar.value()
        ingresado_cop = self.ui.spin_cop_facturar.value()

        if ingresado_bs > bs:
            self.ui.double_bs_facturar.setValue(bs)
            ingresado_bs = bs
        if ingresado_dolar > dolar:
            self.ui.double_dolares_facturar.setValue(dolar)
            ingresado_dolar = dolar
        if ingresado_cop > cop:
            self.ui.spin_cop_facturar.setValue(cop)
            ingresado_cop = cop
        
        restante_dolar = dolar-ingresado_dolar
        restante_bs = bs-ingresado_bs
        restante_cop = cop-ingresado_cop
        print(restante_bs,restante_dolar,restante_cop)
        
        if restante_dolar != dolar:
            restante_bs-=ingresado_dolar*self.tasa_bolivares
            restante_cop-=ingresado_dolar*self.tasa_cop
        
        if restante_bs != bs:
            restante_dolar-=ingresado_bs/self.tasa_bolivares
            restante_cop-=(ingresado_bs/self.tasa_bolivares)*self.tasa_cop
        
        if restante_cop != cop:
            restante_bs-=(ingresado_cop/self.tasa_cop)*self.tasa_bolivares
            restante_dolar-=ingresado_cop/self.tasa_cop
        
        
        self.ui.label_bs.setText(str(round(restante_bs,2)))
        self.ui.label_dolar.setText(str(round(restante_dolar,2)))
        self.ui.label_cop.setText(str(int(round(restante_cop,2))))
        