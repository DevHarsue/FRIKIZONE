from fpdf import FPDF
import os


class CierreMensualPDF(FPDF):
    def __init__(self, año, mes, dias,totales):
        super().__init__()
        self.año = año
        self.mes = mes
        self.dias = dias
        self.totales = totales
        
        
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
        self.cell(0, 10, 'Cierre Mensual', 0, 1, 'C')
        self.cell(0, 10, f'Fecha: {self.año}-{self.mes}', 0, 1, 'C')

    def add_table(self):
        self.cell(20, 20, '',0,1,'C')
        self.set_font('Arial', 'B', 12)
        self.cell(25, 10, 'FECHA', 1)
        self.cell(55, 10, 'BS', 1)
        self.cell(55, 10, 'COP', 1)
        self.cell(55, 10, 'DOLAR', 1)
        self.ln()
        self.set_font('Arial', '', 12)
        
        for dia in self.dias:
            self.cell(25, 10, str(dia[0]), 1)
            self.cell(55, 10, str(dia[1]), 1)
            self.cell(55, 10, str(dia[2]), 1)
            self.cell(55, 10, str(dia[3]), 1)
            self.ln()
        self.cell(25, 10, "Totales", 1)
        self.cell(55, 10, str(self.totales[0][-1]), 1)
        self.cell(55, 10, str(self.totales[1][-1]), 1)
        self.cell(55, 10, str(self.totales[2][-1]), 1)


        
