from submain import MainWindow
from conexion_bd.tablas import TablaDivisas

class VistaDivisas:
    def __init__(self,ventana: MainWindow) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_actualizar_adivisa.pressed.connect(self.actualizar_divisa)
        self.ui.combo_divisa_adivisa.currentIndexChanged.connect(self.cargar_divisa)
        self.cargar_divisa()
    
    def cargar_divisa(self):
        self.indice = self.ui.combo_divisa_adivisa.currentIndex()
        self.divisa = TablaDivisas().select(self.indice+1)[0]
        self.ui.double_valor_adivisa.setValue(self.divisa.relacion)
        if self.indice==1:
            self.ui.double_valor_adivisa.setSingleStep(1000)
        else:
            self.ui.double_valor_adivisa.setSingleStep(1)

        
    
    def actualizar_divisa(self):
        valor = self.ui.double_valor_adivisa.value()
        if valor<=0:
            self.ventana.mostrar_mensaje("Valor Invalido","El valor debe ser mayor a 0")
            return 0
        
        TablaDivisas().update(self.indice+1,{"divisa_relacion":valor})
        self.ventana.mostrar_mensaje("Divisa Actualizada","Divisa actualizada correctamente.")
        self.ventana.vista_facturar.tasa_bolivares = float(TablaDivisas().select(1)[0].relacion)
        self.ventana.vista_facturar.tasa_cop = float(TablaDivisas().select(2)[0].relacion)
        self.ventana.vista_facturar.calcular()
        self.ventana.vista_facturar.calcular_dolar()
        self.ventana.vista_facturar.calcular_bs()
        self.ventana.vista_facturar.calcular_cop()
        