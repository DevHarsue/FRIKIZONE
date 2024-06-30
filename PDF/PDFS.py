from fpdf import FPDF
import os
class CierreMensualPDF(FPDF):
    def __init__(self, fecha_cierre, datos_mensuales):
        super().__init__()
        self.fecha_cierre = fecha_cierre
        self.datos_mensuales = datos_mensuales
        self.total_bolivares = sum(dato['total_bolivares'] for dato in self.datos_mensuales)
        self.total_pesos = sum(dato['total_pesos'] for dato in self.datos_mensuales)
        self.total_dolares = sum(dato['total_dolares'] for dato in self.datos_mensuales)
        
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_logo()
        self.add_title()
        self.add_closure_info()
        self.add_totals()
        self.add_final_totals()  # Asegurarse de que se llame aquí para que se ejecute automáticamente

    def add_logo(self):
        logo_path = 'images/logo.png'
        if os.path.exists(logo_path):
            self.image(logo_path, 10, 8, 33)
        else:
            print(f"Error: No se encontró el archivo {logo_path}")

    def add_title(self):
        self.set_font('Arial', 'B', 20)
        self.cell(0, 10, 'FRIKIZONE', 0, 1, 'C')
        self.set_font('Arial', 'B', 20)
        self.cell(0, 10, 'Cierre Mensual', 0, 1, 'C')
        

    def add_closure_info(self):
        self.ln()
        self.set_font('Arial', '', 20)
        self.cell(0, 10, 'Resumen del Mes', 0, 1, 'C')

    def add_totals(self):
        self.ln()
        self.set_font('Arial', 'B', 12)
        self.cell(40, 10, 'Fecha', 1)
        self.cell(50, 10, 'Total Bolívares', 1)
        self.cell(50, 10, 'Total Pesos', 1)
        self.cell(50, 10, 'Total Dólares', 1)
        self.ln()
        self.set_font('Arial', '', 12)
        
        for dato in self.datos_mensuales:
            self.cell(40, 10, dato['fecha'], 1)
            self.cell(50, 10, f"{dato['total_bolivares']:.2f}", 1)
            self.cell(50, 10, f"{dato['total_pesos']:.2f}", 1)
            self.cell(50, 10, f"{dato['total_dolares']:.2f}", 1)
            self.ln() 
    
    def add_final_totals(self):
        self.set_font('Arial', 'B', 12)
        self.cell(40, 10, 'Total', 1)
        self.cell(50, 10, f"BS:{self.total_bolivares:.2f}", 1)
        self.cell(50, 10, f"COP:{self.total_pesos:.2f}", 1)
        self.cell(50, 10, f"${self.total_dolares:.2f}", 1)  


class ProductoMasVendidosPDF(FPDF):
    def __init__(self, fecha_reporte, productos):
        super().__init__()
        self.fecha_reporte = fecha_reporte
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
        self.cell(0, 10, 'Productos Más Vendidos', 0, 1, 'C')
        self.cell(0, 10, f'Fecha: {self.fecha_reporte}', 0, 1, 'C')

    def add_table(self):
        self.ln()
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


class ProductoMenosVendidosPDF(FPDF):
    def __init__(self, fecha_reporte, productos):
        super().__init__()
        self.fecha_reporte = fecha_reporte
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
        self.cell(0, 10, 'Productos Menos Vendidos', 0, 1, 'C')
        self.cell(0, 10, f'Fecha: {self.fecha_reporte}', 0, 1, 'C')

    def add_table(self):
        self.ln()
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


# Ejemplo de uso

# productos = [
#     {'numero': '001', 'articulo': 'Producto 1', 'descripcion': 'Dragon ball sjfbafhbgajsfvasjavfhasvfhasf 1', 'qty': 2, 'precio': 10.00,"subtotal":200},
#     {'numero': '002', 'articulo': 'Producto 2', 'descripcion': 'peluche de pochita', 'qty': 1, 'precio': 20.00,"subtotal":200},
#     {'numero': '003', 'articulo': 'Producto 1', 'descripcion': 'Dragon ball tomo 2', 'qty': 3, 'precio': 30.00,"subtotal":200},
# ]

# clientes = [
#     {'nombre': 'Cliente Ejemplo 1', 'contacto': '987-654-3210', 'direccion': 'Avenida Siempre Viva 742'},
#     {'nombre': 'Cliente Ejemplo 2', 'contacto': '123-456-7890', 'direccion': 'Calle Falsa 123'},
# ]


# datos_mensuales = [
#     {'fecha': '01/06/2024', 'total_bolivares': 1000.00, 'total_pesos': 5000.00, 'total_dolares': 200.00},
#     {'fecha': '02/06/2024', 'total_bolivares': 1500.00, 'total_pesos': 6000.00, 'total_dolares': 300.00},
#     {'fecha': '04/06/2024', 'total_bolivares': 780.00, 'total_pesos': 20000.00, 'total_dolares': 20.00},
    

    
#     # Agrega más datos según sea necesario
# ]

# productos_mas_vendidos = [
#     {'numero': '001', 'articulo': 'Producto 1', 'descripcion': 'Descripción 1', 'qty': 10, 'precio': 10.00},
#     {'numero': '002', 'articulo': 'Producto 2', 'descripcion': 'Descripción 2', 'qty': 8, 'precio': 15.00},
#     # Agrega más productos según sea necesario
# ]

# productos_menos_vendidos = [
#     {'numero': '003', 'articulo': 'Producto 3', 'descripcion': 'Descripción 3', 'qty': 2, 'precio': 5.00},
#     {'numero': '004', 'articulo': 'Producto 4', 'descripcion': 'Descripción 4', 'qty': 1, 'precio': 12.00},
#     {'numero': '005', 'articulo': 'Producto 5', 'descripcion': 'Descripción 4', 'qty': 1, 'precio': 12.00}
#     # Agrega más productos según sea necesario
# ]


# for cliente in clientes:
#     factura = FacturaPDF(1,
#         datetime.now().strftime('%d/%m/%Y'),
#         cliente['nombre'],
#         cliente['contacto'],
#         cliente['direccion'],
#         productos,"500","398","36","3700"
#     )
#     factura.output(f'factura_{factura.numero_factura}.pdf')

# # Lista de datos para cierres diarios
# cierres_diarios = [
#     {
#         'fecha_cierr': datetime.now().strftime('%d/%m/%Y'),
#         'tasa_bolivares': 24.5,
#         'tasa_pesos': 0.05,
#         'total_bolivares': 2450.00,
#         'total_pesos': 5000.00,
#         'total_dolares': 100.00,
#     }
#     ]

# for cierre in cierres_diarios:
#     cierre_diario = CierreDiarioPDF(
#         fecha_cierre=cierre['fecha_cierr'],
#         tasa_bolivares=cierre['tasa_bolivares'],
#         tasa_pesos=cierre['tasa_pesos'],
#         total_bolivares=cierre['total_bolivares'],
#         total_pesos=cierre['total_pesos'],
#         total_dolares=cierre['total_dolares']
#     )

# cierre_mensual = CierreMensualPDF(
#     fecha_cierre=datetime.now().strftime('%d/%m/%Y'),
#     datos_mensuales=datos_mensuales
# )
# cierre_mensual.output(f'cierre_mensual_{cierre_mensual.fecha_cierre.replace("/", "-")}.pdf')

# producto_mas_vendidos = ProductoMasVendidosPDF(
#     fecha_reporte=datetime.now().strftime('%d/%m/%Y'),
#     productos=productos_mas_vendidos
# )
# producto_mas_vendidos.output(f'productos_mas_vendidos_{producto_mas_vendidos.fecha_reporte.replace("/", "-")}.pdf')

# producto_menos_vendidos = ProductoMenosVendidosPDF(
#     fecha_reporte=datetime.now().strftime('%d/%m/%Y'),
#     productos=productos_menos_vendidos
# )
# producto_menos_vendidos.output(f'productos_menos_vendidos_{producto_menos_vendidos.fecha_reporte.replace("/", "-")}.pdf')            
                 
                                 