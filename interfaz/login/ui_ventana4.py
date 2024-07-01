# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana4.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_VentanaRegistro(object):
    def setupUi(self, VentanaRegistro):
        if not VentanaRegistro.objectName():
            VentanaRegistro.setObjectName(u"VentanaRegistro")
        VentanaRegistro.resize(700, 537)
        VentanaRegistro.setMinimumSize(QSize(700, 500))
        VentanaRegistro.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"images/zone.ico", QSize(), QIcon.Normal, QIcon.Off)
        VentanaRegistro.setWindowIcon(icon)
        VentanaRegistro.setStyleSheet(u"QWidget#centralwidget{\n"
"background: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.511, y2:1, stop:0 rgba(20, 20, 02, 100), stop:1 rgba(12, 38, 60, 1))\n"
"}\n"
"\n"
"\n"
"QFrame{\n"
"	background-color:transparent;\n"
"	border:none;\n"
"}\n"
"\n"
"QlineEdit{\n"
"	background:red;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background: transparent;\n"
"	border: none;\n"
"	min-width: 2em;\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border: 1px dashed white;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"	background:rgba(57, 215, 200,0.8);\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 85, 255);	\n"
"	outline: none;\n"
"}")
        self.centralwidget = QWidget(VentanaRegistro)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(700, 500))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(700, 500))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 40, 0, 0)
        self.interfaz_registro = QFrame(self.frame)
        self.interfaz_registro.setObjectName(u"interfaz_registro")
        self.label = QLabel(self.interfaz_registro)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 0, 456, 53))
        self.label.setMaximumSize(QSize(600, 60))
        self.label.setStyleSheet(u"font: 30pt \"Sylfaen\";\n"
"color:rgb(85, 255, 255);")
        self.frame_2 = QFrame(self.interfaz_registro)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 110, 320, 300))
        self.frame_2.setMinimumSize(QSize(320, 200))
        self.frame_2.setMaximumSize(QSize(400, 16777215))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(8, 5, 0, 5)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(200, 50))
        self.label_5.setStyleSheet(u"QLabel{\n"
"	color:rgba(85, 255, 255,1)\n"
"}\n"
"")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(200, 50))
        self.label_6.setStyleSheet(u"QLabel{\n"
"	color:rgba(85, 255, 255,1)\n"
"}\n"
"")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 2)

        self.line_confirmar = QLineEdit(self.frame_2)
        self.line_confirmar.setObjectName(u"line_confirmar")
        self.line_confirmar.setMinimumSize(QSize(300, 22))
        self.line_confirmar.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setStrikeOut(False)
        self.line_confirmar.setFont(font)
        self.line_confirmar.setStyleSheet(u"QLineEdit{\n"
"	color:rgb(85, 255, 255);\n"
"	background:rgba(10,12,30,0.8);\n"
"	border-style:none;\n"
"	border-radius:8px\n"
"}\n"
"")
        self.line_confirmar.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.line_confirmar, 7, 0, 1, 2)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 50))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color:rgba(85, 255, 255,1)\n"
"}\n"
"")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(100, 40))
        self.frame_3.setMaximumSize(QSize(100, 40))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.boton_registrar = QPushButton(self.frame_3)
        self.boton_registrar.setObjectName(u"boton_registrar")
        self.boton_registrar.setGeometry(QRect(10, 10, 75, 24))
        self.boton_registrar.setMinimumSize(QSize(75, 24))
        self.boton_registrar.setMaximumSize(QSize(75, 24))
        self.boton_registrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_registrar.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"	color: white;\n"
"	background-color: rgba(57, 215, 200,0.8);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(57, 225, 180,0.8);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(57, 210, 168,0.8);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.frame_3, 8, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.line_contrasena = QLineEdit(self.frame_2)
        self.line_contrasena.setObjectName(u"line_contrasena")
        self.line_contrasena.setMinimumSize(QSize(300, 22))
        self.line_contrasena.setMaximumSize(QSize(300, 16777215))
        self.line_contrasena.setFont(font)
        self.line_contrasena.setStyleSheet(u"QLineEdit{\n"
"	color:rgb(85, 255, 255);\n"
"	background:rgba(10,12,30,0.8);\n"
"	border-style:none;\n"
"	border-radius:8px\n"
"}\n"
"")
        self.line_contrasena.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.line_contrasena, 5, 0, 1, 2)

        self.line_usuario = QLineEdit(self.frame_2)
        self.line_usuario.setObjectName(u"line_usuario")
        self.line_usuario.setMinimumSize(QSize(300, 22))
        self.line_usuario.setMaximumSize(QSize(300, 16777215))
        self.line_usuario.setFont(font)
        self.line_usuario.setStyleSheet(u"QLineEdit{\n"
"	color:rgb(85, 255, 255);\n"
"	background:rgba(10,12,30,0.8);\n"
"	border-style:none;\n"
"	border-radius:8px\n"
"}\n"
"")

        self.gridLayout.addWidget(self.line_usuario, 3, 0, 1, 2)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(32, 20))
        self.comboBox.setMaximumSize(QSize(120, 20))
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(u"")

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 2)

        self.frame_4 = QFrame(self.interfaz_registro)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(360, 110, 320, 274))
        self.frame_4.setMinimumSize(QSize(320, 200))
        self.frame_4.setMaximumSize(QSize(320, 16777215))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.imagen = QLabel(self.frame_4)
        self.imagen.setObjectName(u"imagen")
        self.imagen.setPixmap(QPixmap(u"images/sincara_icon.png"))
        self.imagen.setScaledContents(True)

        self.verticalLayout.addWidget(self.imagen)

        self.boton_volver = QPushButton(self.interfaz_registro)
        self.boton_volver.setObjectName(u"boton_volver")
        self.boton_volver.setEnabled(False)
        self.boton_volver.setGeometry(QRect(300, 460, 75, 24))
        self.boton_volver.setMinimumSize(QSize(75, 24))
        self.boton_volver.setMaximumSize(QSize(75, 24))
        self.boton_volver.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_volver.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"	color: white;\n"
"	background-color: rgba(57, 215, 200,0.8);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(57, 225, 180,0.8);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(57, 210, 168,0.8);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgba(47, 200, 180,0.8);\n"
"	color: gray;\n"
"}\n"
"")
        self.label.raise_()
        self.frame_4.raise_()
        self.boton_volver.raise_()
        self.frame_2.raise_()

        self.verticalLayout_3.addWidget(self.interfaz_registro)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignHCenter)

        VentanaRegistro.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.comboBox, self.line_usuario)
        QWidget.setTabOrder(self.line_usuario, self.line_contrasena)
        QWidget.setTabOrder(self.line_contrasena, self.line_confirmar)
        QWidget.setTabOrder(self.line_confirmar, self.boton_registrar)
        QWidget.setTabOrder(self.boton_registrar, self.boton_volver)

        self.retranslateUi(VentanaRegistro)

        QMetaObject.connectSlotsByName(VentanaRegistro)
    # setupUi

    def retranslateUi(self, VentanaRegistro):
        VentanaRegistro.setWindowTitle(QCoreApplication.translate("VentanaRegistro", u"FRIKIZONE", None))
        self.label.setText(QCoreApplication.translate("VentanaRegistro", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">REGISTRO DE USUARIO</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("VentanaRegistro", u"Contrase\u00f1a:", None))
        self.label_6.setText(QCoreApplication.translate("VentanaRegistro", u"Confirmar Contrase\u00f1a:", None))
        self.line_confirmar.setText("")
        self.label_2.setText(QCoreApplication.translate("VentanaRegistro", u"Nombre (Usuario):", None))
        self.boton_registrar.setText(QCoreApplication.translate("VentanaRegistro", u"REGISTRAR", None))
        self.line_contrasena.setText("")
        self.line_usuario.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("VentanaRegistro", u"SUPERADMIN", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("VentanaRegistro", u"ADMIN", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("VentanaRegistro", u"USER", None))

        self.imagen.setText("")
        self.boton_volver.setText(QCoreApplication.translate("VentanaRegistro", u"VOLVER", None))
    # retranslateUi

