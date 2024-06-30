from submain import MainWindow
from conexion_bd.tablas import TablaTotalesDiarios,TablaVentas,TablaVentasIngresos
from PySide6.QtCore import QDate
from PySide6.QtWidgets import QTableWidgetItem
from utilidades.funciones_utiles import obtener_fecha
from PDF.cierre import CierreDiarioPDF
import os
import webbrowser

class VistaCierre:
    def __init__(self,ventana: MainWindow) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_buscar_cierre.pressed.connect(self.buscar)
        self.ui.boton_realizar_cierre.pressed.connect(self.cierre)
        self.ui.botont_rehacer_cierre.pressed.connect(self.rehacer)
        self.ui.date_cierre.dateChanged.connect(self.reiniciar)
        self.tabla = TablaTotalesDiarios()
        self.tabla_ventas = TablaVentas()
        fecha = obtener_fecha().split("-")
        self.ui.date_cierre.setDate(QDate(int(fecha[0]),int(fecha[1]),int(fecha[2])))
        
    def buscar(self):
        self.reiniciar()
        self.fecha = self.ui.date_cierre.date().toString("yyyy-MM-dd")
        totales = self.tabla.select_fecha(self.fecha)
        if bool(totales):
            self.ventana.mostrar_mensaje("Cierre Encontrado","Este dia ya ha sido cerrado")
            self.ui.botont_rehacer_cierre.setEnabled(True)
            self.ui.label_bs_cierre.setText(str(totales[0].total))
            self.ui.label_cop_cierre.setText(str(totales[1].total))
            self.ui.label_dolar_cierre.setText(str(totales[2].total))
        else:
            totales = self.tabla.calcular_diario(self.fecha)
            if not bool(totales):
                self.ventana.mostrar_mensaje("No hay Ventas","Este dia no tiene ventas")
                return 0
            self.ui.boton_realizar_cierre.setEnabled(True)
            self.ui.label_bs_cierre.setText(str(totales[0][-1]))
            self.ui.label_cop_cierre.setText(str(totales[1][-1]))
            self.ui.label_dolar_cierre.setText(str(totales[2][-1]))
        
        self.cargar_facturas()
    
    def cargar_facturas(self):
        self.ventas = self.tabla_ventas.select_fecha(self.fecha)
        tabla = TablaVentasIngresos()
        bs=0
        cop=0
        dolar=0
        self.datos_imprimir = []
        for i,venta in enumerate(self.ventas):
            self.ventana.ui.table_facturas_cierre.insertRow(self.ventana.ui.table_facturas_cierre.rowCount())
            self.ventana.ui.table_facturas_cierre.setItem(i,0,QTableWidgetItem(str(venta.id)))
            self.ventana.ui.table_facturas_cierre.setItem(i,1,QTableWidgetItem(str(venta.cliente_id)))
            total = tabla.select_venta(venta.id)
            self.ventana.ui.table_facturas_cierre.setItem(i,2,QTableWidgetItem(str(total[0].cantidad)))
            self.ventana.ui.table_facturas_cierre.setItem(i,3,QTableWidgetItem(str(total[1].cantidad)))
            self.ventana.ui.table_facturas_cierre.setItem(i,4,QTableWidgetItem(str(total[2].cantidad)))
            self.datos_imprimir.append({"ID":venta.id,"CEDULA":venta.cliente_id,"BS":total[0].cantidad,"COP":total[1].cantidad,"DOLAR":total[2].cantidad})
            bs+=total[0].cantidad
            cop+=total[1].cantidad
            dolar+=total[2].cantidad
        
        if str(bs)!=self.ui.label_bs_cierre.text():
            self.ui.label_bs_cierre.setStyleSheet("color: red")
        if str(cop)!=self.ui.label_cop_cierre.text():
            self.ui.label_cop_cierre.setStyleSheet("color: red")
        if str(dolar)!=self.ui.label_dolar_cierre.text():
            self.ui.label_dolar_cierre.setStyleSheet("color: red")

    
    def cierre(self):
        self.ventana.preguntar("Realizar Cierre","¿Estas seguro de realizar el cierre?")
        if not self.ventana.respuesta:
            return 0
        bs = self.ui.label_bs_cierre.text()
        cop = self.ui.label_cop_cierre.text()
        dolar = self.ui.label_dolar_cierre.text()
        self.tabla.insert(self.fecha,1,bs)
        self.tabla.insert(self.fecha,2,cop)
        self.tabla.insert(self.fecha,3,dolar)
        
        self.ventana.mostrar_mensaje("Cierre Realizado","Cierre Realizado Correctamente")
        self.imprimir(self.fecha,bs,cop,dolar)
        
        self.reiniciar()
    
    def rehacer(self):
        self.ventana.preguntar("Rehacer Cierre","¿Estas Seguro de Realizar Nuevamente el Cierre?")
        if not self.ventana.respuesta:
            return 0
        totales_ant = self.tabla.select_fecha(self.fecha)
        totales = self.tabla.calcular_diario(self.fecha)
        if not bool(totales):
            self.ventana.preguntar("Sin Ventas","No se han encontrado ventas\n¿Se borrara el cierre estas de acuerdo?")
            if not self.ventana.respuesta:
                return 0
            self.tabla.delete(totales_ant[0].id)
            self.tabla.delete(totales_ant[1].id)
            self.tabla.delete(totales_ant[2].id)
            self.reiniciar()
            self.ventana.mostrar_mensaje("Cierre Borrado","Cierre Borrado Exitosamente")
            return 0
            
        self.tabla.update(totales_ant[0].id,{"total_diario_cantidad":totales[0][-1]})
        self.tabla.update(totales_ant[1].id,{"total_diario_cantidad":totales[1][-1]})
        self.tabla.update(totales_ant[2].id,{"total_diario_cantidad":totales[2][-1]})
        self.ventana.mostrar_mensaje("Cierre Actualizado","Cierre Realizado Exitosamente")
        self.reiniciar()
        self.ui.label_bs_cierre.setText(str(totales[0][-1]))
        self.ui.label_cop_cierre.setText(str(totales[1][-1]))
        self.ui.label_dolar_cierre.setText(str(totales[2][-1]))
        self.imprimir(self.fecha,str(totales[0][-1]),str(totales[1][-1]),str(totales[2][-1]))
        self.ui.botont_rehacer_cierre.setEnabled(True)
        self.cargar_facturas()
    
    def reiniciar(self):
        while self.ui.table_facturas_cierre.rowCount()>0:
            self.ui.table_facturas_cierre.removeRow(0)
        
        self.ui.label_cop_cierre.setText("")
        self.ui.label_bs_cierre.setText("")
        self.ui.label_dolar_cierre.setText("")
        self.ui.label_bs_cierre.setStyleSheet("")
        self.ui.label_cop_cierre.setStyleSheet("")
        self.ui.label_dolar_cierre.setStyleSheet("")
        
        self.ui.boton_realizar_cierre.setDisabled(True)
        self.ui.botont_rehacer_cierre.setDisabled(True)
    
    def imprimir(self,fecha,bs,cop,dolar):
        
        pdf = CierreDiarioPDF(fecha,bs,cop,dolar,self.datos_imprimir)
        documentos_path = str(os.path.expanduser("~\\Documents"))
        try:
            os.makedirs(documentos_path+"\\FRIKIZONE")
        except FileExistsError:
            pass
        path = f"{documentos_path}\\FRIKIZONE\\cierre_{fecha}.pdf"
        pdf.output(path)
        webbrowser.open_new(path)