import sys
from PyQt6 import QtWidgets, uic
from PyQt6.uic import loadUi

# Iniciar la aplicación
app = QtWidgets.QApplication([])

# Cargar archivos .ui
login = uic.loadUi("interfaz_ui/ventana1.ui")
entrar = uic.loadUi("interfaz_ui/ventana2.ui")
error = uic.loadUi("interfaz_ui/ventana3.ui")
registro = uic.loadUi("interfaz_ui/ventana4.ui")


############################## FUNCIONES ##############################


# Funciones para interfaz Login VENTANA1

def gui_login():
    name = login.lineEdit_1.text().upper()
    password = login.lineEdit_2.text()

    if len(name) == 0 or len(password) == 0:
        login.label.setText("¡Ingrese Todos los datos!")

    elif name == "STEVEN" and password == "0000":
        gui_entrar()

    else:
        gui_error()

# Funciones para interfaz entrar VENTANA2

def gui_entrar():
    login.hide()
    entrar.show()

def regresar_entrar():
    entrar.hide()
    login.label.setText(" ")
    login.show()

# Funciones para interfaz error VENTANA3

def gui_error():
    login.hide()
    error.show()

def regresar_error():
    error.hide()
    login.label.setText(" ")
    login.show()

# Funciones para interfaz registro VENTANA4

def registrar():
    error.hide()
    registro.show()
    nombre = registro.lineEdit.text()
    cedula = registro.lineEdit_2.int()
    telefono = registro.lineEdit_3.int()
    clave = registro.lineEdit_4.text()
    confirmar_clave = registro.lineEdit_5.text()


# Función para cerrar ventana 

def salir():
    app.exit()

def reinicio():
    app.exit()

############################## BOTONES ##############################

# Botones login
login.pushButton.clicked.connect(gui_login)

login.pushButton_2.clicked.connect(salir)

# Botones Entrar

entrar.pushButton.clicked.connect(regresar_entrar)

entrar.pushButton_2.clicked.connect(salir)

# Botones Error

error.pushButton.clicked.connect(regresar_error)

error.pushButton_2.clicked.connect(salir)

# Botones registro

error.pushButton_3.clicked.connect(registrar)



# Ejecutable
registro.show()
app.exec()

