# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana1LzneYQ.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 508)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
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
        self.centralwidget.setMinimumSize(QSize(700, 500))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet(u"#frame_2{\n"
"	border: none;\n"
"}\n"
"\n"
"#frame{\n"
"	border: none;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(700, 500))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.BotonSalir = QPushButton(self.frame)
        self.BotonSalir.setObjectName(u"BotonSalir")
        self.BotonSalir.setGeometry(QRect(585, 467, 75, 24))
        self.BotonSalir.setMinimumSize(QSize(75, 24))
        self.BotonSalir.setMaximumSize(QSize(75, 24))
        self.BotonSalir.setCursor(QCursor(Qt.PointingHandCursor))
        self.BotonSalir.setStyleSheet(u"QPushButton{\n"
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
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 681, 489))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(self.layoutWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(261, 101))
        self.widget.setMaximumSize(QSize(16777215, 80))
        self.widget.setStyleSheet(u"")
        self.Nombre_Empresa = QLabel(self.widget)
        self.Nombre_Empresa.setObjectName(u"Nombre_Empresa")
        self.Nombre_Empresa.setGeometry(QRect(-225, -30, 701, 181))
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

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(300, 50))
        self.label.setMaximumSize(QSize(300, 40))
        self.label.setStyleSheet(u"font: 600 9pt \"Segoe UI\";\n"
"color: rgb(255, 2, 2);\n"
"\n"
"font: 11pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label, 5, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.BotonLogin = QPushButton(self.layoutWidget)
        self.BotonLogin.setObjectName(u"BotonLogin")
        self.BotonLogin.setMinimumSize(QSize(75, 24))
        self.BotonLogin.setMaximumSize(QSize(75, 24))
        self.BotonLogin.setCursor(QCursor(Qt.PointingHandCursor))
        self.BotonLogin.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout.addWidget(self.BotonLogin, 3, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.frame_2 = QFrame(self.layoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 120))
        self.frame_2.setMaximumSize(QSize(300, 140))
        self.frame_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.Clave = QLineEdit(self.frame_2)
        self.Clave.setObjectName(u"Clave")
        self.Clave.setEnabled(True)
        self.Clave.setGeometry(QRect(97, 80, 200, 25))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Clave.sizePolicy().hasHeightForWidth())
        self.Clave.setSizePolicy(sizePolicy)
        self.Clave.setMinimumSize(QSize(200, 25))
        self.Clave.setMaximumSize(QSize(200, 20))
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
        self.Clave.setPalette(palette)
        self.Clave.setCursor(QCursor(Qt.IBeamCursor))
        self.Clave.setMouseTracking(True)
        self.Clave.setTabletTracking(False)
        self.Clave.setAcceptDrops(True)
        self.Clave.setAutoFillBackground(False)
        self.Clave.setStyleSheet(u"border-radius:8px;\n"
"background-color: rgba(0, 0, 20,0.5);\n"
"color:rgba(85, 249, 255,0.8);\n"
"font: 700 9pt \"Segoe UI\";")
        self.Clave.setFrame(True)
        self.Clave.setEchoMode(QLineEdit.EchoMode.Password)
        self.Clave.setDragEnabled(True)
        self.Clave.setReadOnly(False)
        self.Clave.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.Clave.setClearButtonEnabled(False)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(9, 60, 82, 61))
        self.label_5.setMinimumSize(QSize(81, 61))
        self.label_5.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.Usuario = QLineEdit(self.frame_2)
        self.Usuario.setObjectName(u"Usuario")
        self.Usuario.setEnabled(True)
        self.Usuario.setGeometry(QRect(97, 20, 200, 25))
        sizePolicy.setHeightForWidth(self.Usuario.sizePolicy().hasHeightForWidth())
        self.Usuario.setSizePolicy(sizePolicy)
        self.Usuario.setMinimumSize(QSize(200, 25))
        self.Usuario.setMaximumSize(QSize(200, 20))
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
        self.Usuario.setPalette(palette1)
        self.Usuario.setMouseTracking(True)
        self.Usuario.setTabletTracking(False)
        self.Usuario.setAcceptDrops(True)
        self.Usuario.setAutoFillBackground(False)
        self.Usuario.setStyleSheet(u"border-radius:8px;\n"
"background-color: rgba(0, 0, 20,0.5);\n"
"color:rgba(85, 249, 255,0.7);\n"
"font: 700 9pt \"Segoe UI\";")
        self.Usuario.setFrame(True)
        self.Usuario.setEchoMode(QLineEdit.EchoMode.Normal)
        self.Usuario.setDragEnabled(True)
        self.Usuario.setReadOnly(False)
        self.Usuario.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.Usuario.setClearButtonEnabled(False)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(9, 0, 81, 61))
        self.label_4.setMinimumSize(QSize(81, 61))
        self.label_4.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.usuario_incorrecto = QLabel(self.frame_2)
        self.usuario_incorrecto.setObjectName(u"usuario_incorrecto")
        self.usuario_incorrecto.setGeometry(QRect(100, 50, 190, 16))
        self.usuario_incorrecto.setMinimumSize(QSize(190, 16))
        self.usuario_incorrecto.setMaximumSize(QSize(190, 16))
        self.usuario_incorrecto.setStyleSheet(u"color:red;")
        self.clave_incorrecta = QLabel(self.frame_2)
        self.clave_incorrecta.setObjectName(u"clave_incorrecta")
        self.clave_incorrecta.setGeometry(QRect(100, 110, 190, 16))
        self.clave_incorrecta.setMinimumSize(QSize(190, 16))
        self.clave_incorrecta.setMaximumSize(QSize(190, 16))
        self.clave_incorrecta.setStyleSheet(u"color:red;")

        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(350, 60))
        self.label_3.setMaximumSize(QSize(350, 40))
        self.label_3.setStyleSheet(u"font: 14pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.BotonRegistro = QPushButton(self.layoutWidget)
        self.BotonRegistro.setObjectName(u"BotonRegistro")
        self.BotonRegistro.setMinimumSize(QSize(75, 24))
        self.BotonRegistro.setMaximumSize(QSize(75, 24))
        self.BotonRegistro.setCursor(QCursor(Qt.PointingHandCursor))
        self.BotonRegistro.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"	color: white;\n"
"	background-color: rgba(170, 235, 255,0.8);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(97, 225, 200,0.8);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(57, 210, 168,0.8);\n"
"}\n"
"\n"
"font: 700 9pt \"Segoe UI\";\n"
"\n"
"")

        self.gridLayout.addWidget(self.BotonRegistro, 4, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.layoutWidget.raise_()
        self.BotonSalir.raise_()

        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.Usuario, self.Clave)
        QWidget.setTabOrder(self.Clave, self.BotonSalir)

        self.retranslateUi(MainWindow)
        self.BotonSalir.pressed.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.BotonSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.BotonLogin.setText(QCoreApplication.translate("MainWindow", u"Ingresar", None))
        self.Clave.setText("")
        self.Clave.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Ingrese su contrase\u00f1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Contrase\u00f1a:</p></body></html>", None))
        self.Usuario.setText("")
        self.Usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Ingrese su usuario", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Usuario:</p></body></html>", None))
        self.usuario_incorrecto.setText("")
        self.clave_incorrecta.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Ingrese sus datos de usuario, por favor.</p></body></html>", None))
        self.BotonRegistro.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
    # retranslateUi

