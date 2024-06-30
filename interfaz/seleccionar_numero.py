# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seleccionar_numero.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Cantidad(object):
    def setupUi(self, Cantidad):
        if not Cantidad.objectName():
            Cantidad.setObjectName(u"Cantidad")
        Cantidad.resize(370, 80)
        Cantidad.setMaximumSize(QSize(370, 80))
        icon = QIcon()
        icon.addFile(u"images/zone.ico", QSize(), QIcon.Normal, QIcon.Off)
        Cantidad.setWindowIcon(icon)
        Cantidad.setStyleSheet(u"*{\n"
"	font-size: 12px;\n"
"	font-family: Rockwell;\n"
"}\n"
"\n"
"#Cantidad{background: url(\"images/fondo_messagebox.png\")}\n"
"#centralwidget{\n"
"	background: rgba(0,0,0,240)\n"
"}\n"
"QPushButton{\n"
"	border: none;\n"
"	padding: 0.2em 1em 0.2em 1em;\n"
"	background: transparent;\n"
"	border-bottom: 1px solid white;\n"
"	border-top: 1px solid white;\n"
"	min-width: 8em;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-color: rgb(0, 255, 255);\n"
"	color: rgb(0,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	border-color: rgb(0, 85, 255);\n"
"	color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"	background: transparent;\n"
"	font-size: 13px;\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"QDoubleSpinBox, QSpinBox,QDateEdit {\n"
"	min-width: 8em;\n"
"    padding-right: 25px; \n"
"	border: none;\n"
"    border-bottom: 1px solid white;\n"
"	background: transparent;\n"
"	selection-color: rgb(0, 255, 255);\n"
"	selection-background-color: rg"
                        "ba(0, 0, 0, 200);\n"
"}\n"
"\n"
"QDoubleSpinBox:focus,QSpinBox:focus,QDateEdit:focus {\n"
"	border-color: rgb(0, 255, 255);\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"        border: 1px solid white;\n"
"        width:10px;\n"
"        margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
" background: rgb(0, 255, 255);\n"
"min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}")
        self.verticalLayout = QVBoxLayout(Cantidad)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.centralwidget = QWidget(Cantidad)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(999)

        self.gridLayout.addWidget(self.spinBox, 1, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonBox.setOrientation(Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 0, 1, 2, 1)


        self.verticalLayout.addWidget(self.centralwidget)


        self.retranslateUi(Cantidad)

        QMetaObject.connectSlotsByName(Cantidad)
    # setupUi

    def retranslateUi(self, Cantidad):
        Cantidad.setWindowTitle(QCoreApplication.translate("Cantidad", u"SELECCIONE CANTIDAD", None))
        self.label.setText(QCoreApplication.translate("Cantidad", u"Cantidad:", None))
    # retranslateUi

