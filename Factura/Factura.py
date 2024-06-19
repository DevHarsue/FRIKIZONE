from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        
        pdf.set_text_color(0, 0, 100)

        self.image('logo.png', 10, 8, 33)
        
        self.set_font('Arial', 'B', 30)
    
        self.cell(0, 10, 'FACTURA', 0, 1, 'C')
       
        self.ln(30)

    def footer(self):
        
        self.set_y(-15)
        
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'No Requiere Firma', 0, 1, 'C')

#
pdf = PDF()

# Add a page
pdf.add_page()


pdf.set_font('Arial', '', 12)
pdf.set_text_color(0, 100, 0)


# Invoice data in one line
pdf.cell(63, 10, 'Numero de Factura:', 0, 0)
pdf.cell(63, 10, 'Fecha: ', 0, 0)
pdf.cell(0, 10, 'Nombre del Supervisor: ', 0, 1)

# Datos de la factura
pdf.cell(63, 10, '12345', 0, 0)
pdf.cell(63, 10, '18/06/2024', 0, 0)
pdf.cell(0, 10, 'Juan Perez', 0, 1)

# Line break
pdf.ln(10)


pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'FACTURA A:', 0, 1)
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'Nombre: Cliente Ejemplo', 0, 1)
pdf.cell(0, 10, 'Contacto: 123456789', 0, 1)
pdf.cell(0, 10, 'Direccion: Calle Falsa 123', 0, 1)

# Salto de linea 
pdf.ln(10)


pdf.set_font('Arial', 'B', 12)
pdf.cell(30, 10, 'Numero', 1)
pdf.cell(50, 10, 'ARTICULO', 1)
pdf.cell(60, 10, 'DESCRIPCION', 1)
pdf.cell(20, 10, 'QTY', 1)
pdf.cell(30, 10, 'Precio', 1)
pdf.ln()


pdf.set_font('Arial', '', 12)


pdf.cell(30, 10, '', 1)
pdf.cell(50, 10, '', 1)
pdf.cell(60, 10, '', 1)
pdf.cell(20, 10, '', 1)
pdf.cell(30, 10, '', 1)
pdf.ln()


pdf.cell(160, 10, 'Total a pagar:', 1)
pdf.cell(30, 10, '', 1)
pdf.ln(20)

# metodos de pago 
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Formas de pago:', 0, 1)
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'Nombre del Banco: Banco Venezuela', 0, 1)
pdf.cell(0, 10, 'Titular de la Cuenta: Hakari kInji ', 0, 1)

# Detalles del pie de pagina 
pdf.ln(10)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'FRIKIZONE', 0, 1)
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'Contacto: xxxxxxxx', 0, 1)
pdf.cell(0, 10, 'Direccion: Centro Civico', 0, 1)

# Output the PDF
pdf.output('factura.pdf')