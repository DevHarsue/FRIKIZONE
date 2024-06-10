from PyQt6 import QtWidgets, uic

#Iniciar la aplicación
app = QtWidgets.QApplication([])

# Cargar los archivos .ui
login = uic.load_ui("Ventana1.ui")
entrar = uic.load_ui("ventana2.ui")
error = uic.load_ui("ventana3.ui")

# Ejecutable
login.show()
app.exec()