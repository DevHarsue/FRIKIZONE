import re

class Validador():
    def __init__(self):
        self.validar_string_regex = r'^[a-zA-Z]+$'
        self.users = r'^[a-zA-Z0-9_]{8,}$'
        self.Password = r'^(?=.*[A-Z])(?=.*[a-zA-Z0-9])(?=.*[@$!#%?&]{2,})[A-Za-z\d@$!#%?&]{8,}$'
        self.num_telefono =r'^(0412|0414|0424|0416|0426)(-?\d{7}){1}$|^\+57(-?\d{10}){1}$'

    def validar_string(self, nombre):
        return bool(re.match(self.validar_string_regex, nombre))

    def usuarios(self, usuario):
        return bool(re.match(self.users, usuario))
    
    def contraseña(self, password):
        return bool(re.match(self.Password, password))

    def telefono(self,phone):
        return bool(re.match(self.num_telefono,phone))