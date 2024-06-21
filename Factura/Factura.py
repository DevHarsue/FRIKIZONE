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


class CierreDiarioPDF(FPDF):
    def __init__(self, fecha_cierre, tasa_bolivares, tasa_pesos, total_bolivares, total_pesos, total_dolares):
        super().__init__()
        self.fecha_cierre = fecha_cierre
        self.tasa_bolivares = tasa_bolivares
        self.tasa_pesos = tasa_pesos
        self.total_bolivares = total_bolivares
        self.total_pesos = total_pesos
        self.total_dolares = total_dolares
        
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_logo()
        self.add_title()
        self.add_closure_info()
        self.add_totals()

    def add_logo(self):
        logo_path = 'logo.png'
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

    def add_closure_info(self):
        self.ln()
        self.set_font('Arial', '', 20)
        self.cell(0, 10, f'Tasa de Bolívares: {self.tasa_bolivares}', 0, 1, 'C')
        self.cell(0, 10, f'Tasa de Pesos: {self.tasa_pesos}', 0, 1, 'C')

    def add_totals(self):
        self.ln()
        self.set_font('Arial', 'B', 20)
        self.cell(0, 10, 'Totales:', 0, 1, 'C')
        self.set_font('Arial', '', 20)
        self.cell(0, 10, f'Total en Bolívares: {self.total_bolivares}', 0, 1, 'C')
        self.cell(0, 10, f'Total en Pesos: {self.total_pesos}', 0, 1, 'C')
        self.cell(0, 10, f'Total en Dólares: {self.total_dolares}', 0, 1, 'C')


# Example usage
productos = [
    {'numero': '001', 'articulo': 'Producto 1', 'descripcion': 'Dragon ball tomo 1', 'qty': 2, 'precio': 10.00},
    {'numero': '002', 'articulo': 'Producto 2', 'descripcion': 'peluche de pochita', 'qty': 1, 'precio': 20.00},
    {'numero': '003', 'articulo': 'Producto 1', 'descripcion': 'Dragon ball tomo 2', 'qty': 3, 'precio': 30.00},
]

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

# Lista de datos para cierres diarios
cierres_diarios = [
    {
        'fecha_cierr': datetime.now().strftime('%d/%m/%Y'),
        'tasa_bolivares': 24.5,
        'tasa_pesos': 0.05,
        'total_bolivares': 2450.00,
        'total_pesos': 5000.00,
        'total_dolares': 100.00,
    }
    ]
for cierre in cierres_diarios:
    cierre_diario = CierreDiarioPDF(
        fecha_cierre=cierre['fecha_cierr'],
        tasa_bolivares=cierre['tasa_bolivares'],
        tasa_pesos=cierre['tasa_pesos'],
        total_bolivares=cierre['total_bolivares'],
        total_pesos=cierre['total_pesos'],
        total_dolares=cierre['total_dolares']
    )
    cierre_diario.output(f'cierre_diario_{cierre["fecha_cierr"].replace("/", "-")}.pdf')