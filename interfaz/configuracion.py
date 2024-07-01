# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_BD.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_VentanaConfiguracion(object):
    def setupUi(self, VentanaConfiguracion):
        if not VentanaConfiguracion.objectName():
            VentanaConfiguracion.setObjectName(u"VentanaConfiguracion")
        VentanaConfiguracion.resize(700, 560)
        VentanaConfiguracion.setMinimumSize(QSize(700, 500))
        VentanaConfiguracion.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"images/zone.ico", QSize(), QIcon.Normal, QIcon.Off)
        VentanaConfiguracion.setWindowIcon(icon)
        VentanaConfiguracion.setStyleSheet(u"QWidget#centralwidget{\n"
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
"}")
        self.centralwidget = QWidget(VentanaConfiguracion)
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
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QLineEdit{\n"
"	color:rgb(85, 255, 255);\n"
"	background:rgba(10,12,30,0.8);\n"
"	border-style:none;\n"
"	border-radius:8px\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"	background:rgba(10,12,20,0.8);\n"
"	color: gray;\n"
"}")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 50))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color:rgba(85, 255, 255,1);\n"
"	font: 20pt \"Segoe UI\";\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line_usuario = QLineEdit(self.widget)
        self.line_usuario.setObjectName(u"line_usuario")
        self.line_usuario.setMinimumSize(QSize(250, 22))
        self.line_usuario.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setStrikeOut(False)
        self.line_usuario.setFont(font)
        self.line_usuario.setStyleSheet(u"")
        self.line_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.line_usuario, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(200, 50))
        self.label_4.setStyleSheet(u"QLabel{\n"
"	color:rgba(85, 255, 255,1);\n"
"	font: 20pt \"Segoe UI\";\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line_host = QLineEdit(self.widget)
        self.line_host.setObjectName(u"line_host")
        self.line_host.setEnabled(True)
        self.line_host.setMinimumSize(QSize(250, 22))
        self.line_host.setMaximumSize(QSize(300, 16777215))
        self.line_host.setFont(font)
        self.line_host.setStyleSheet(u"")
        self.line_host.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.line_host, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(200, 50))
        self.label_5.setStyleSheet(u"QLabel{\n"
"	color:rgba(85, 255, 255,1);\n"
"	font: 20pt \"Segoe UI\";\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line_port = QLineEdit(self.widget)
        self.line_port.setObjectName(u"line_port")
        self.line_port.setEnabled(True)
        self.line_port.setMinimumSize(QSize(250, 22))
        self.line_port.setMaximumSize(QSize(300, 16777215))
        self.line_port.setFont(font)
        self.line_port.setStyleSheet(u"")
        self.line_port.setEchoMode(QLineEdit.EchoMode.Normal)
        self.line_port.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.line_port, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(200, 50))
        self.label_6.setStyleSheet(u"QLabel{\n"
"	color:rgba(85, 255, 255,1);\n"
"	font: 20pt \"Segoe UI\";\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line_contrasena = QLineEdit(self.widget)
        self.line_contrasena.setObjectName(u"line_contrasena")
        self.line_contrasena.setMinimumSize(QSize(250, 22))
        self.line_contrasena.setMaximumSize(QSize(300, 16777215))
        self.line_contrasena.setFont(font)
        self.line_contrasena.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.line_contrasena.setStyleSheet(u"")
        self.line_contrasena.setEchoMode(QLineEdit.EchoMode.Password)
        self.line_contrasena.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.line_contrasena, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(600, 60))
        self.label.setStyleSheet(u"font: 30pt \"Sylfaen\";\n"
"color:rgb(85, 255, 255);")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(320, 200))
        self.frame_4.setMaximumSize(QSize(320, 16777215))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.imagen = QLabel(self.frame_4)
        self.imagen.setObjectName(u"imagen")
        self.imagen.setMinimumSize(QSize(302, 370))
        self.imagen.setPixmap(QPixmap(u"images/logo.png"))
        self.imagen.setScaledContents(True)
        self.imagen.setWordWrap(False)

        self.horizontalLayout.addWidget(self.imagen)


        self.gridLayout.addWidget(self.frame_4, 1, 3, 1, 1)

        self.boton_volver = QPushButton(self.widget)
        self.boton_volver.setObjectName(u"boton_volver")
        self.boton_volver.setEnabled(False)
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
"QPushButton:disabled{\n"
"	background-color: rgba(47, 200, 180,0.8);\n"
"	color: gray;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.boton_volver, 2, 3, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.boton_conectar = QPushButton(self.widget)
        self.boton_conectar.setObjectName(u"boton_conectar")
        self.boton_conectar.setMinimumSize(QSize(75, 24))
        self.boton_conectar.setMaximumSize(QSize(75, 24))
        self.boton_conectar.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_conectar.setStyleSheet(u"\n"
"QPushButton{\n"
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

        self.gridLayout.addWidget(self.boton_conectar, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_3.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignHCenter)

        VentanaConfiguracion.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.line_usuario, self.line_host)
        QWidget.setTabOrder(self.line_host, self.line_port)
        QWidget.setTabOrder(self.line_port, self.line_contrasena)
        QWidget.setTabOrder(self.line_contrasena, self.boton_conectar)
        QWidget.setTabOrder(self.boton_conectar, self.boton_volver)

        self.retranslateUi(VentanaConfiguracion)

        QMetaObject.connectSlotsByName(VentanaConfiguracion)
    # setupUi

    def retranslateUi(self, VentanaConfiguracion):
        VentanaConfiguracion.setWindowTitle(QCoreApplication.translate("VentanaConfiguracion", u"FRIKIZONE", None))
        self.label_2.setText(QCoreApplication.translate("VentanaConfiguracion", u"Usuario", None))
#if QT_CONFIG(tooltip)
        self.line_usuario.setToolTip(QCoreApplication.translate("VentanaConfiguracion", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.line_usuario.setText("")
        self.label_4.setText(QCoreApplication.translate("VentanaConfiguracion", u"Host", None))
        self.line_host.setText("")
        self.label_5.setText(QCoreApplication.translate("VentanaConfiguracion", u"Port", None))
        self.line_port.setText("")
        self.label_6.setText(QCoreApplication.translate("VentanaConfiguracion", u"Contrase\u00f1a", None))
        self.line_contrasena.setText("")
        self.label.setText(QCoreApplication.translate("VentanaConfiguracion", u"<html><head/><body><p align=\"center\">USUARIO BASE DE DATOS</p><p align=\"center\"><br/></p></body></html>", None))
        self.imagen.setText("")
        self.boton_volver.setText(QCoreApplication.translate("VentanaConfiguracion", u"VOLVER", None))
        self.boton_conectar.setText(QCoreApplication.translate("VentanaConfiguracion", u"CONECTAR", None))
    # retranslateUi

