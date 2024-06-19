import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QStackedWidget
from PyQt6.uic import loadUi
from ui_ventana1 import Ui_MainWindow as Ventana1, QPushButton
from ui_ventana2 import Ui_MainWindow as Ventana2

class MainWindow(QMainWindow):
    def __init__(self):
        super(Ventana1, self).__init__()
        loadUi("Ventana1", self)
        self.button.clicked.connect(self.abrir_ventana)

    def abrir_ventana(self):
        widget.setCurrentIndex(widget.currentIndex()+1)


class ventana_2(QDialog):
        def __init__(self):
            super(Ventana2, self).__init__()
            loadUi("Ventana2", self)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
ventana2 = ventana_2()
widget.addWidget(mainwindow)
widget.addWidget(ventana2)
widget.setFixedHeight(300)
widget.setFixedWidth(400)
widget.show()

        