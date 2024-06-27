# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_BDKEKUzI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import imagenes_rc
import imagenes_rc

class Ui_VentanaRegistro(object):
    def setupUi(self, VentanaRegistro):
        if not VentanaRegistro.objectName():
            VentanaRegistro.setObjectName(u"VentanaRegistro")
        VentanaRegistro.resize(700, 560)
        VentanaRegistro.setMinimumSize(QSize(700, 500))
        VentanaRegistro.setMaximumSize(QSize(16777215, 16777215))
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
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.gridlayout = QGridLayout(self.widget)
        self.gridlayout.setObjectName(u"gridlayout")
        self.gridlayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridlayout.setHorizontalSpacing(10)
        self.gridlayout.setVerticalSpacing(20)
        self.gridlayout.setContentsMargins(15, 15, 15, 10)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(600, 60))
        self.label.setStyleSheet(u"font: 30pt \"Sylfaen\";\n"
"color:rgb(85, 255, 255);")

        self.gridlayout.addWidget(self.label, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

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

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(250, 22))
        self.lineEdit.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setStrikeOut(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	color:rgb(85, 255, 255);\n"
"	background:rgba(10,12,30,0.8);\n"
"	border-style:none;\n"
"	border-radius:8px\n"
"}\n"
"")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(200, 50))
        self.label_4.setStyleSheet(u"QLabel{\n"
"	color:rgba(85, 255, 255,1);\n"
"	font: 20pt \"Segoe UI\";\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(250, 22))
        self.lineEdit_3.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	color:rgb(85, 255, 255);\n"
"	background:rgba(10,12,30,0.8);\n"
"	border-style:none;\n"
"	border-radius:8px\n"
"}\n"
"")
        self.lineEdit_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(200, 50))
        self.label_5.setStyleSheet(u"QLabel{\n"
"	color:rgba(85, 255, 255,1);\n"
"	font: 20pt \"Segoe UI\";\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(250, 22))
        self.lineEdit_4.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"	color:rgb(85, 255, 255);\n"
"	background:rgba(10,12,30,0.8);\n"
"	border-style:none;\n"
"	border-radius:8px\n"
"}\n"
"")
        self.lineEdit_4.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(200, 50))
        self.label_6.setStyleSheet(u"QLabel{\n"
"	color:rgba(85, 255, 255,1);\n"
"	font: 20pt \"Segoe UI\";\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(250, 22))
        self.lineEdit_5.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_5.setStyleSheet(u"QLineEdit{\n"
"	color:rgb(85, 255, 255);\n"
"	background:rgba(10,12,30,0.8);\n"
"	border-style:none;\n"
"	border-radius:8px\n"
"}\n"
"")
        self.lineEdit_5.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_5, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridlayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(75, 24))
        self.pushButton.setMaximumSize(QSize(75, 24))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
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

        self.gridlayout.addWidget(self.pushButton, 2, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

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
        self.imagen.setPixmap(QPixmap(u"../images/logo.png"))
        self.imagen.setScaledContents(True)
        self.imagen.setWordWrap(False)

        self.horizontalLayout.addWidget(self.imagen)


        self.gridlayout.addWidget(self.frame_4, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignHCenter)

        VentanaRegistro.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.lineEdit_5)

        self.retranslateUi(VentanaRegistro)

        QMetaObject.connectSlotsByName(VentanaRegistro)
    # setupUi

    def retranslateUi(self, VentanaRegistro):
        VentanaRegistro.setWindowTitle(QCoreApplication.translate("VentanaRegistro", u"Registro", None))
        self.label.setText(QCoreApplication.translate("VentanaRegistro", u"<html><head/><body><p align=\"center\">USUARIO BASE DE DATOS</p><p align=\"center\"><br/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("VentanaRegistro", u"Usuario", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("VentanaRegistro", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit.setText("")
        self.label_4.setText(QCoreApplication.translate("VentanaRegistro", u"Host", None))
        self.lineEdit_3.setText("")
        self.label_5.setText(QCoreApplication.translate("VentanaRegistro", u"Port", None))
        self.lineEdit_4.setText("")
        self.label_6.setText(QCoreApplication.translate("VentanaRegistro", u"Contrase\u00f1a", None))
        self.lineEdit_5.setText("")
        self.pushButton.setText(QCoreApplication.translate("VentanaRegistro", u"INGRESAR", None))
        self.imagen.setText("")
    # retranslateUi

