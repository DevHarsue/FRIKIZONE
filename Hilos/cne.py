from PySide6.QtCore import QObject, QThread, Signal
from Hilos.scrapping_web_cne import BuscadorPersonas
import requests

class HiloCNE(QThread):
    persona = Signal(list)
    error = Signal(Exception)
    terminar = Signal()
    def __init__(self,nacionalidad,cedula) -> None:
        super().__init__()
        self.nacionalidad = nacionalidad
        self.cedula = cedula
    
    def run(self):
        buscador = BuscadorPersonas()
        try:
            persona = buscador.buscar_persona(self.nacionalidad,self.cedula)
            if isinstance(persona,Exception):
                raise persona
            self.persona.emit(persona)
        except Exception as e:
            if isinstance(e,requests.exceptions.ConnectionError):
                self.error.emit(ErrorConexion(e))
            elif str(e) == "list index out of range":
                self.error.emit(ErrorPersona(e))
            else:
                self.error.emit(e)
        self.terminar.emit()

class ErrorConexion(Exception):
    def __init__(self,error):
        super().__init__(f"Problema de conexion")
        self.e = error
        
class ErrorPersona(Exception):
    def __init__(self,error):
        super().__init__(f"La Persona no fue encontrada en el CNE")
        self.e = error
