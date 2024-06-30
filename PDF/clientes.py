from fpdf import FPDF
import os


class ClientesPDF(FPDF):
    def __init__(self, año,mes,clientes):
        super().__init__()
        self.año = año
        self.mes = mes
        self.clientes = clientes
        
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
        self.cell(0, 10, 'Clientes Frecuentes', 0, 1, 'C')
        self.cell(0, 10, f'Fecha: {self.mes}/{self.año}', 0, 1, 'C')

    def add_table(self):
        self.cell(20, 20, '',0,1,'C')
        self.set_font('Arial', 'B', 12)
        self.cell(10, 10, 'ID', 1)
        self.cell(25, 10, 'CEDULA', 1)
        self.cell(30, 10, 'NOMBRE', 1)
        self.cell(30, 10, 'APELLIDO', 1)
        self.cell(20, 10, 'BS', 1)
        self.cell(30, 10, 'COP', 1)
        self.cell(20, 10, 'DOLAR', 1)
        self.cell(25, 10, 'FACTURAS', 1)
        self.ln()
        self.set_font('Arial', '', 12)
        
        for cliente in self.clientes:
            self.cell(10, 10, str(cliente[0]), 1)
            self.cell(25, 10, str(cliente[1]), 1)
            self.cell(30, 10, str(cliente[2]), 1)
            self.cell(30, 10, str(cliente[3]), 1)
            self.cell(20, 10, str(cliente[4]), 1)
            self.cell(30, 10, str(cliente[5]), 1)
            self.cell(20, 10, str(cliente[6]), 1)
            self.cell(25, 10, str(cliente[7]), 1)
            self.ln()


        
