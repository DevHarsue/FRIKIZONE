from fpdf import FPDF
import os
from datetime import datetime

class FacturaPDF(FPDF):
    invoice_counter = 0  # Class variable to keep track of invoice numbers

    def __init__(self, fecha_factura, nombre_supervisor, nombre_cliente, contacto_cliente, direccion_cliente, productos):
        super().__init__()
        FacturaPDF.invoice_counter += 1  # Increment the invoice counter
        self.numero_factura = FacturaPDF.invoice_counter
        self.fecha_factura = fecha_factura
        self.nombre_supervisor = nombre_supervisor
        self.nombre_cliente = nombre_cliente
        self.contacto_cliente = contacto_cliente
        self.direccion_cliente = direccion_cliente
        self.productos = productos
        
        self.total = 0
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_logo()
        self.add_title()
        self.add_invoice_info()
        self.add_client_info()
        self.add_table()
        self.add_footer()

    def add_logo(self):
        logo_path = 'logo.png'
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
        self.cell(0, 10, f'Supervisor: {self.nombre_supervisor}', 0, 1, 'C')

    def add_client_info(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'FACTURA A:', 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Nombre: {self.nombre_cliente}', 0, 1, 'L')
        self.cell(0, 10, f'Contacto: {self.contacto_cliente}', 0, 1, 'L')
        self.cell(0, 10, f'Dirección: {self.direccion_cliente}', 0, 1, 'L')

    def add_table(self):
        self.set_font('Arial', 'B', 12)
        self.cell(30, 10, 'Número', 1)
        self.cell(55, 10, 'Artículo', 1)
        self.cell(55, 10, 'Descripción', 1)
        self.cell(20, 10, 'QTY', 1)
        self.cell(30, 10, 'Precio', 1)
        self.ln()
        self.set_font('Arial', '', 12)
        
        for producto in self.productos:
            self.cell(30, 10, producto['numero'], 1)
            self.cell(55, 10, producto['articulo'], 1)
            self.cell(55, 10, producto['descripcion'], 1)
            self.cell(20, 10, str(producto['qty']), 1)
            self.cell(30, 10, f"${producto['precio']:.2f}", 1)
            self.ln()
            self.total += producto['precio'] * producto['qty']
        self.cell(160, 10, 'Total a Pagar', 1)
        self.cell(30, 10, f"${self.total:.2f}", 1)

    def add_footer(self):
        self.set_y(250)
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'No Requiere Firma', 0, 1, 'C')
        
      

productos = [
    {'numero': '001', 'articulo': 'Producto 1', 'descripcion': 'Dragon ball tomo 1', 'qty': 2, 'precio': 10.00},
    {'numero': '002', 'articulo': 'Producto 2', 'descripcion': 'peluche de pochita', 'qty': 1, 'precio': 20.00},
    {'numero': '003', 'articulo': 'Producto 1', 'descripcion': 'Dragon ball tomo 2', 'qty': 3, 'precio': 30.00},
]

# genera 2 factursa con sus repectivos datos 
clientes = [
    {'nombre': 'Cliente Ejemplo 1', 'contacto': '987-654-3210', 'direccion': 'Avenida Siempre Viva 742'},
    {'nombre': 'Cliente Ejemplo 2', 'contacto': '123-456-7890', 'direccion': 'Calle Falsa 123'},
]

for cliente in clientes:
    factura = FacturaPDF(
        fecha_factura=datetime.now().strftime('%d/%m/%Y'),
        nombre_supervisor='Juan Pérez',
        nombre_cliente=cliente['nombre'],
        contacto_cliente=cliente['contacto'],
        direccion_cliente=cliente['direccion'],
        productos=productos,
        
    )
    factura.output(f'factura_{factura.numero_factura}.pdf')