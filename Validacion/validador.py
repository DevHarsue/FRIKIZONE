from PySide6.QtWidgets import QApplication, QLineEdit
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

class Validador:
    def __init__(self):
        self.regex_solo_texto = QRegularExpression(r"^[A-Za-z]+$")
        self.regex_numero_telefono = QRegularExpression(r"^[0-9\-\+]{15}$")
        self.regex_cedula = QRegularExpression(r"^[0-9]{9}$")

    def solo_texto(self,line):
        line.setValidator(QRegularExpressionValidator(self.regex_solo_texto))
    
    def numero_telefono(self,line):
        line.setValidator(QRegularExpressionValidator(self.regex_numero_telefono))
        
    def cedulas(self,line):
        line.setValidator(QRegularExpressionValidator(self.regex_cedula))
        