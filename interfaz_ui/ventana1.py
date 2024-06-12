# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana1.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QWidget)

class Ui_MainWindow_2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setMaximumSize(QSize(700, 500))
        font = QFont()
        font.setPointSize(6)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"background: qlineargradient(spread:pad, x1:0.517, y1:0, x2:0.511, y2:1, stop:0 rgba(20, 20, 02, 100), stop:1 rgba(12, 38, 60, 1))\n"
"}\n"
"")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 150, 371, 71))
        self.label_3.setStyleSheet(u"font: 14pt \"Segoe UI\";")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(210, 200, 81, 61))
        self.label_4.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(230, 50, 261, 101))
        self.widget.setStyleSheet(u"")
        self.Nombre_Empresa = QLabel(self.widget)
        self.Nombre_Empresa.setObjectName(u"Nombre_Empresa")
        self.Nombre_Empresa.setGeometry(QRect(-220, -30, 701, 181))
        self.Nombre_Empresa.setStyleSheet(u"font: 700 36pt \"Sylfaen\";\n"
"\n"
"color: rgb(55, 255, 248);")
        self.Nombre_empresa2 = QLabel(self.widget)
        self.Nombre_empresa2.setObjectName(u"Nombre_empresa2")
        self.Nombre_empresa2.setGeometry(QRect(-200, -10, 671, 161))
        self.Nombre_empresa2.setAutoFillBackground(False)
        self.Nombre_empresa2.setStyleSheet(u"font: 36pt \"Sylfaen\";\n"
"color: rgba(10, 100, 80,0.2);\n"
"background:transparent;")
        self.Nombre_empresa2.raise_()
        self.Nombre_Empresa.raise_()
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 240, 91, 61))
        self.label_5.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QRect(300, 260, 200, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaximumSize(QSize(200, 20))
        palette = QPalette()
        brush = QBrush(QColor(10, 199, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 20, 127))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(10, 199, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_2.setPalette(palette)
        self.lineEdit_2.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit_2.setMouseTracking(True)
        self.lineEdit_2.setTabletTracking(False)
        self.lineEdit_2.setAcceptDrops(True)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet(u"border-radius:8px;\n"
"background-color: rgba(0, 0, 20,0.5);\n"
"color:rgba(85, 249, 255,0.8);\n"
"font: 700 9pt \"Segoe UI\";")
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_2.setDragEnabled(True)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_1 = QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setEnabled(True)
        self.lineEdit_1.setGeometry(QRect(300, 220, 200, 20))
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setMaximumSize(QSize(200, 20))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_1.setPalette(palette1)
        self.lineEdit_1.setMouseTracking(True)
        self.lineEdit_1.setTabletTracking(False)
        self.lineEdit_1.setAcceptDrops(True)
        self.lineEdit_1.setAutoFillBackground(False)
        self.lineEdit_1.setStyleSheet(u"border-radius:8px;\n"
"background-color: rgba(0, 0, 20,0.5);\n"
"color:rgba(85, 249, 255,0.7);\n"
"font: 700 9pt \"Segoe UI\";")
        self.lineEdit_1.setFrame(True)
        self.lineEdit_1.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_1.setDragEnabled(True)
        self.lineEdit_1.setReadOnly(False)
        self.lineEdit_1.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.lineEdit_1.setClearButtonEnabled(False)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(430, 290, 75, 24))
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
"\n"
"font: 700 9pt \"Segoe UI\";\n"
"\n"
"")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(600, 460, 75, 24))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
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
"font: 700 9pt \"Segoe UI\";\n"
"\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 330, 231, 16))
        self.label.setStyleSheet(u"font: 600 9pt \"Segoe UI\";\n"
"color: rgb(255, 2, 2);\n"
"\n"
"font: 11pt \"Segoe UI\";")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Ingrese sus datos de usuario, por favor.</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Usuario:</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.widget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.widget.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.Nombre_Empresa.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Nombre_Empresa.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Nombre_Empresa.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">FRIKIZONE</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.Nombre_empresa2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Nombre_empresa2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Nombre_empresa2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">FRIKIZONE </p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Contrase\u00f1a:</p></body></html>", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Ingrese su contrase\u00f1a", None))
        self.lineEdit_1.setText("")
        self.lineEdit_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Ingrese su usuario", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ingresar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.label.setText("")
    # retranslateUi

