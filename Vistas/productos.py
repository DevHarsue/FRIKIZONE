from conexion_bd.tablas import TablaProductos
from PySide6.QtWidgets import QDialog,QTableWidgetItem
from interfaz.seleccionar_numero import Ui_Cantidad
from submain import MainWindow

class VistaProductos:
    def __init__(self,ventana: MainWindow) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.line_bproducto.textChanged.connect(self.buscar_producto)
        self.ui.combo_buscar_bproducto.currentIndexChanged.connect(self.cambiar_place_holder)
        self.ui.table_productos.itemEntered.connect(self.item_clickeado)
        self.ui.table_productos.itemPressed.connect(self.item_clickeado)
        self.compra = False
        self.buscar_producto()
    
    def buscar_producto(self):
        while self.ui.table_productos.rowCount() > 0:
            self.ui.table_productos.removeRow(0)
        producto = self.ui.line_bproducto.text()
        texto_combo = self.ui.combo_buscar_bproducto.currentText()
        if texto_combo == "ID":
            try:
                id_producto = int(producto)
                producto = TablaProductos().select(id_producto)
            except Exception as e:
                return 0
            
        elif texto_combo == "NOMBRE":
            producto = TablaProductos().select_nombre(producto)
        
        if bool(producto):
            for i,x in enumerate(producto):
                self.ui.table_productos.insertRow(self.ui.table_productos.rowCount())
                self.ui.table_productos.setItem(i,0,QTableWidgetItem(str(x.id)))
                self.ui.table_productos.setItem(i,1,QTableWidgetItem(str(x.nombre)))
                self.ui.table_productos.setItem(i,2,QTableWidgetItem(str(x.descripcion)))
                self.ui.table_productos.setItem(i,3,QTableWidgetItem(str(x.valor)))
        
    def cambiar_place_holder(self):
        self.ui.line_bproducto.setPlaceholderText(self.ui.combo_buscar_bproducto.currentText())
    
    def item_clickeado(self):
        row = self.ui.table_productos.currentRow()
        self.datos = []
        for x in range(4):
            self.datos.append(self.ui.table_productos.item(row,x).text())
        
        if self.compra:
            self.dialogo = NumberInputDialog(self)
            self.dialogo.show()
        
            
    

class NumberInputDialog(QDialog):
    def __init__(self,ventana):
        super().__init__()
        self.setModal(True)
        self.ventana = ventana
        self.ui = Ui_Cantidad()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.dar_cantidad)
        self.ui.buttonBox.rejected.connect(self.close)
    
    def dar_cantidad(self):
        self.ventana.cantidad = self.ui.spinBox.value()
        if self.ui.spinBox.value()<=0:
            self.no_producto()
            return 0
        self.ventana.ui.stacked_widget.setCurrentWidget(self.ventana.ui.vista_facturar)
        self.ventana.ventana.vista_facturar.meter_producto()
        self.close()
        self.ventana.compra = False
        
    def no_producto(self):
        self.ventana.ventana.mostrar_mensaje("Cantidad Invalida","La cantidad tiene que ser mayor a 0")
        self.close()

