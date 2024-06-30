from fpdf import FPDF
import os

class FacturaPDF(FPDF):
    def __init__(self, numero_factura,fecha_factura, cedula, nombre_cliente, contacto_cliente, direccion_cliente, productos,total,total_sin_iva,total_dolares,total_bs,total_cop):
        super().__init__()
        self.numero_factura = numero_factura
        self.fecha_factura = fecha_factura
        self.cedula = cedula
        self.nombre_cliente = nombre_cliente
        self.contacto_cliente = contacto_cliente
        self.direccion_cliente = direccion_cliente
        self.productos = productos
        self.total = total
        self.total_sin_iva = total_sin_iva
        self.total_dolares = total_dolares
        self.total_bs = total_bs
        self.total_cop = total_cop
        
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_logo()
        self.add_title()
        self.add_invoice_info()
        self.add_client_info()
        self.add_table()
        self.add_footer()

    def add_logo(self):
        logo_path = 'images/logo.png'
        if os.path.exists(logo_path):
            self.image(logo_path, 10, 8, 33)
        else:
            print(f"Error: No se encontró el archivo {logo_path}")

    def add_title(self):
        self.set_font('Arial', 'B', 20)
        self.cell(0, 10, 'FACTURA', 0, 1, 'C')
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'FRIKIZONE', 0, 1, 'C')
        self.cell(0,10,'Carrera 8 con Calle 8, Centro de la Ciudad',0,1,'C')

    def add_invoice_info(self):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'Contacto: +58 412-1281711', 0, 1, 'C')
        self.cell(0, 10, f'Número de Factura: {self.numero_factura}', 0, 1, 'C')
        self.cell(0, 10, f'Fecha: {self.fecha_factura}', 0, 1, 'C')

    def add_client_info(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'FACTURA A:', 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Cedula: {self.cedula}', 0, 1, 'L')
        self.cell(0, 10, f'Nombre: {self.nombre_cliente}', 0, 1, 'L')
        self.cell(0, 10, f'Contacto: {self.contacto_cliente}', 0, 1, 'L')
        self.cell(0, 10, f'Dirección: {self.direccion_cliente}', 0, 1, 'L')

    def add_table(self):
        self.set_font('Arial', 'B', 12)
        self.cell(20, 10, 'Número', 1)
        self.cell(60, 10, 'Artículo', 1)
        self.cell(40, 10, 'QTY', 1)
        self.cell(30, 10, 'Precio', 1)
        self.cell(40, 10, 'SubTotal', 1)
        self.ln()
        self.set_font('Arial', '', 12)
        
        for producto in self.productos:
            self.cell(20, 10, producto['numero'], 1)
            self.cell(60, 10, producto['articulo'], 1)
            self.cell(40, 10, str(producto['qty']), 1)
            self.cell(30, 10, f"{producto['precio']}$", 1)
            self.cell(40, 10, f"{producto['subtotal']}$", 1)
            self.ln()
        self.cell(150, 10, 'Total', 1)
        self.cell(40, 10, f"{self.total_sin_iva}$", 1)
        self.ln()
        self.cell(150, 10, 'IVA(16%)', 1)
        self.cell(40, 10, f"{round(self.total-self.total_sin_iva,2)}$", 1)
        self.ln()
        self.cell(150, 10, 'Total + IVA(16%)', 1)
        self.cell(40, 10, f"{self.total}$", 1)
        self.ln()
        self.cell(15,10,f"Total Pagado en Dolares: {self.total_dolares}$")
        self.ln()
        self.cell(15,10,f"Total Pagado en Bolivares: {self.total_bs}BS")
        self.ln()
        self.cell(15,10,f"Total Pagado en COP: {self.total_cop}COP")
        self.ln()
    def add_footer(self):
        self.set_y(250)
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'No Requiere Firma', 0, 1, 'C')