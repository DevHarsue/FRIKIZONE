from submain import MainWindow
from utilidades.funciones_utiles import obtener_fecha
from conexion_bd.tablas import TablaClientes,TablaProductos,TablaTotalesDiarios
from PySide6.QtCore import QDate
from PDF.clientes import ClientesPDF
import os
import webbrowser

class VistaData:
    def __init__(self, ventana: MainWindow):
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_cliente_data.pressed.connect(self.clientes)
        self.ui.boton_mensual_data.pressed.connect(self.mes)
        self.ui.boton_producto_data.pressed.connect(self.producto)
        self.informe_mes = False
        self.informe_cliente = False
        self.informe_producto = False
        fecha = obtener_fecha().split("-")
        self.ui.date_mensual.setDate(QDate(int(fecha[0]),int(fecha[1]),1))
        self.ui.boton_generar_informe.pressed.connect(self.generar)
        
    
    def cambiar_vista(self):
        self.ui.stacked_widget.setCurrentWidget(self.ui.vista_mensual)
    
    def clientes(self):
        self.cambiar_vista()
        self.informe_cliente = True
        self.informe_mes = False
        self.informe_producto = False
    
    def mes(self):
        self.cambiar_vista()
        self.informe_mes = True
        self.informe_cliente = False
        self.informe_producto = False
    
    def producto(self):
        self.cambiar_vista()
        self.informe_producto = True
        self.informe_mes = False
        self.informe_cliente = False
        
    def generar(self):
        fecha = self.ui.date_mensual.date().toString("yyyy-MM").split("-")
        if self.informe_cliente:
            clientes = TablaClientes().calcular_clientes(fecha[0],fecha[1])
            if not bool(clientes):
                self.ventana.mostrar_mensaje("Sin Informacion","No hay informacion para la fecha seleccionada")
                return 0
            
            clientes_ids = set()
            for x in clientes:
                clientes_ids.add(x[0])
            
            clientes_imprimir = []
            clientes_ids =tuple(clientes_ids)
            for c in clientes_ids:
                cliente_temp = tuple(filter(lambda x: x[0]==c,clientes))
                clientes_imprimir.append((c,cliente_temp[0][1],cliente_temp[0][2],cliente_temp[0][3],cliente_temp[0][-1],cliente_temp[1][-1],cliente_temp[2][-1]))
            clientes_frecuentes = TablaClientes().calcular_frecuencia_clientes(fecha[0],fecha[1])
            clientes_ordenados = []
            for x,veces in clientes_frecuentes:
                z = list(filter(lambda y: y[0]==x,clientes_imprimir))
                z = list(z[0])
                z.append(veces)
                clientes_ordenados.append(tuple(z))
            self.imprimir_clientes(clientes_ordenados)
    
    def imprimir_clientes(self,clientes):
        fecha = self.ui.date_mensual.date().toString("yyyy-MM").split("-")
        pdf = ClientesPDF(fecha[0],fecha[1],clientes)
        documentos_path = str(os.path.expanduser("~\\Documents"))
        try:
            os.makedirs(documentos_path+"\\FRIKIZONE")
        except FileExistsError:
            pass
        path = f"{documentos_path}\\FRIKIZONE\\clientes_frecuentes_{fecha[0]}-{fecha[1]}.pdf"
        pdf.output(path)
        webbrowser.open_new(path)