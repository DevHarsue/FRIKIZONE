from fpdf import FPDF
import os


class CierreDiarioPDF(FPDF):
    def __init__(self, fecha_cierre, total_bolivares, total_pesos, total_dolares,ventas):
        super().__init__()
        self.fecha_cierre = fecha_cierre
        self.total_bolivares = total_bolivares
        self.total_pesos = total_pesos
        self.total_dolares = total_dolares
        self.ventas = ventas
        
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_logo()
        self.add_title()
        self.add_table()

    def add_logo(self):
        logo_path = 'images/logo.png'
        if os.path.exists(logo_path):
            self.image(logo_path, 10, 8, 33)
        else:
            print(f"Error: No se encontró el archivo {logo_path}")

    def add_title(self):
        self.set_font('Arial', 'B', 20)
        self.cell(0, 10, 'FRIKIZONE', 0, 1, 'C')
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Cierre Diario', 0, 1, 'C')
        self.cell(0, 10, f'Fecha: {self.fecha_cierre}', 0, 1, 'C')

    def add_table(self):
        self.cell(20, 20, '',0,1,'C')
        self.set_font('Arial', 'B', 12)
        self.cell(10, 10, 'ID', 1)
        self.cell(60, 10, 'CEDULA', 1)
        self.cell(40, 10, 'BS', 1)
        self.cell(40, 10, 'COP', 1)
        self.cell(40, 10, 'DOLAR', 1)
        self.ln()
        self.set_font('Arial', '', 12)
        
        for venta in self.ventas:
            self.cell(10, 10, str(venta["ID"]), 1)
            self.cell(60, 10, str(venta["CEDULA"]), 1)
            self.cell(40, 10, str(venta["BS"]), 1)
            self.cell(40, 10, str(venta["COP"]), 1)
            self.cell(40, 10, str(venta["DOLAR"]), 1)
            self.ln()
        self.cell(70, 10, "Totales", 1)
        self.cell(40, 10, str(self.total_bolivares), 1)
        self.cell(40, 10, str(self.total_pesos), 1)
        self.cell(40, 10, str(self.total_dolares), 1)


        
