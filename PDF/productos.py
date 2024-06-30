from fpdf import FPDF
import os


class ProductosPDF(FPDF):
    def __init__(self, año, mes, productos):
        super().__init__()
        self.año = año
        self.mes = mes
        self.productos = productos
        
        
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
        self.cell(0, 10, 'Productos', 0, 1, 'C')
        self.cell(0, 10, f'Fecha: {self.año}-{self.mes}', 0, 1, 'C')

    def add_table(self):
        self.cell(20, 20, '',0,1,'C')
        self.set_font('Arial', 'B', 12)
        self.cell(30, 10, 'ID', 1)
        self.cell(100, 10, 'NOMBRE', 1)
        self.cell(60, 10, 'CANTIDAD', 1)
        self.ln()
        self.set_font('Arial', '', 12)
        
        for producto in self.productos:
            self.cell(30, 10, str(producto[0]), 1)
            self.cell(100, 10, str(producto[1]), 1)
            self.cell(60, 10, str(producto[2]), 1)
            self.ln()


        
