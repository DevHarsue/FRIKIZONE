from PySide6.QtCore import QThread, Signal
from conexion_bd.creador_bd_frikizone import CrearEnv

class HiloEnv(QThread):
    status = Signal(bool)
    def __init__(self,usuario,contraseña,host,puerto) -> None:
        super().__init__()
        self.usuario = usuario
        self.contraseña = contraseña
        self.host = host
        self.puerto = puerto
    
    def run(self):
        env = CrearEnv()
        try:
            testeo = env.testear(self.usuario,self.contraseña,self.host,self.puerto)
            if testeo:
                self.status.emit(True)
            else:
                self.status.emit(False)
                
        except Exception as e:
            print(e)
            self.status.emit(False)

