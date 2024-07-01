from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
import re

class Validador:
    def __init__(self):
        self.regex_solo_texto = QRegularExpression(r"^[A-Za-z]+$")
        self.regex_solo_texto_productos = QRegularExpression(r"^[A-Za-z ]+$")
        self.regex_numero_telefono = QRegularExpression(r"^[0-9\-\+]{15}$")
        self.regex_cedula = QRegularExpression(r"^[0-9]{9}$")
        self.regex_contraseñas = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-+_!@#$%/<>·3()=?¿^&*.,¡`*¨´,_º'^:;ª|~€¬]).{8,}$"
        self.regex_usuarios = QRegularExpression(r"^[A-Za-z0-9_]{15}$")

    def solo_texto(self,line):
        line.setValidator(QRegularExpressionValidator(self.regex_solo_texto))
    
    def solo_texto_productos(self,line):
        line.setValidator(QRegularExpressionValidator(self.regex_solo_texto_productos))
    
    def numero_telefono(self,line):
        line.setValidator(QRegularExpressionValidator(self.regex_numero_telefono))
        
    def cedulas(self,line):
        line.setValidator(QRegularExpressionValidator(self.regex_cedula))

    def usuarios(self,line):
        line.setValidator(QRegularExpressionValidator(self.regex_usuarios))
    
    def comprobar_contraseña(self,contraseña):
        return re.match(self.regex_contraseñas,contraseña)
        
        