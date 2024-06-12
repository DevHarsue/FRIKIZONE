# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_principal.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"*{\n"
"	font-size: 12px;\n"
"	font-family: Sylfaen;\n"
"}\n"
"\n"
"#centralwidget{background: url(\"images/fondo.png\")}\n"
"#contenedor_principal{\n"
"	background: rgba(0,0,0,200)\n"
"}\n"
"\n"
"#widget_lateral QPushButton, #widget_superior QWidget QPushButton{\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	width: 100%;\n"
"	padding: 1em 8px;\n"
"}\n"
"\n"
"#widget_superior QWidget QPushButton{\n"
"	border: none;\n"
"	border-right: 1px solid white;\n"
"}\n"
"\n"
"#widget_lateral QPushButton:hover, #widget_superior QWidget QPushButton:hover{\n"
"	border-color: rgb(0, 255, 255);\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"#widget_lateral QPushButton:pressed, #widget_superior QWidget QPushButton:pressed{\n"
"	border-color: rgb(17, 165, 237);\n"
"	color: rgb(17, 165, 237);\n"
"}\n"
"\n"
"#stacked_widget QWidget{\n"
"	background: rgba(0,0,0,200);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.contenedor_principal = QWidget(self.centralwidget)
        self.contenedor_principal.setObjectName(u"contenedor_principal")
        self.contenedor_principal.setStyleSheet(u"#stacked_widget #facturar #NACIONALIDAD{\n"
"	background: transparent;\n"
"	border: none;\n"
"	min-width: 2em;\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"#stacked_widget #facturar #NACIONALIDAD:focus{\n"
"	border: 1px dashed white;\n"
"}\n"
"\n"
"\n"
"#stacked_widget #facturar #NACIONALIDAD QAbstractItemView{\n"
"	background: transparent;\n"
"	border: none;\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"#stacked_widget #facturar #NACIONALIDAD QAbstractItemView::item:selected {\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 85, 255);	\n"
"	outline: none;\n"
"}\n"
"\n"
"#stacked_widget #facturar QLineEdit{\n"
"	background: transparent;\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	padding: 0.6em 0.4em;\n"
"	color: rgb(0, 255, 255);\n"
"	font-size: 13px;\n"
"}\n"
"\n"
"#stacked_widget #facturar QLineEdit:focus{\n"
"	border-color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"#stacked_widget #facturar QLineEdit:disabled{\n"
"	color: rgb(0, 0, 255);\n"
"}\n"
"\n"
"#stacked_widget #facturar #EDITAR::indicat"
                        "or:checked{\n"
"	image: url(\"images/lock.png\");\n"
"	width: 25px;\n"
"}\n"
"\n"
"#stacked_widget #facturar #EDITAR::indicator:unchecked{\n"
"	image: url(\"images/unlock.png\");\n"
"	width: 25px;\n"
"}\n"
"\n"
"#stacked_widget #facturar QPushButton{\n"
"	border: none;\n"
"	padding: 0.2em 1em 0.2em 1em;\n"
"	background: transparent;\n"
"	border-bottom: 1px solid white;\n"
"	border-top: 1px solid white;\n"
"	min-width: 6em;\n"
"}\n"
"\n"
"#stacked_widget #facturar QPushButton:hover{\n"
"	border-color: rgb(0, 255, 255);\n"
"	color: rgb(0,255,255);\n"
"}\n"
"\n"
"#stacked_widget #facturar QPushButton:pressed{\n"
"	border-color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"#stacked_widget #facturar QPushButton:disabled{\n"
"	border-color: rgb(0, 85, 255);\n"
"	color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"#stacked_widget #facturar #DIRECCION{\n"
"	color: rgb(0,255,255);\n"
"	border: none;\n"
"}\n"
"\n"
"#stacked_widget #facturar #DIRECCION:focus{\n"
"	border-bottom: 1px solid rgb(0, 255, 255);\n"
"}\n"
"")
        self.contenedor_widgets = QGridLayout(self.contenedor_principal)
        self.contenedor_widgets.setObjectName(u"contenedor_widgets")
        self.widget_superior = QWidget(self.contenedor_principal)
        self.widget_superior.setObjectName(u"widget_superior")
        self.horizontalLayout = QHBoxLayout(self.widget_superior)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, -1, 30, -1)
        self.widget = QWidget(self.widget_superior)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.boton_cierre = QPushButton(self.widget)
        self.boton_cierre.setObjectName(u"boton_cierre")

        self.horizontalLayout_2.addWidget(self.boton_cierre)

        self.boton_configuracion = QPushButton(self.widget)
        self.boton_configuracion.setObjectName(u"boton_configuracion")

        self.horizontalLayout_2.addWidget(self.boton_configuracion)

        self.boton_cerrar_sesion = QPushButton(self.widget)
        self.boton_cerrar_sesion.setObjectName(u"boton_cerrar_sesion")

        self.horizontalLayout_2.addWidget(self.boton_cerrar_sesion)


        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignLeft)

        self.label = QLabel(self.widget_superior)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMaximumSize(QSize(80, 80))
        self.label.setPixmap(QPixmap(u"../../images/logo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)

        self.contenedor_widgets.addWidget(self.widget_superior, 0, 0, 1, 2)

        self.widget_lateral = QWidget(self.contenedor_principal)
        self.widget_lateral.setObjectName(u"widget_lateral")
        self.verticalLayout = QVBoxLayout(self.widget_lateral)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 0, 8, 0)
        self.boton_facturar = QPushButton(self.widget_lateral)
        self.boton_facturar.setObjectName(u"boton_facturar")

        self.verticalLayout.addWidget(self.boton_facturar)

        self.boton_clientes = QPushButton(self.widget_lateral)
        self.boton_clientes.setObjectName(u"boton_clientes")

        self.verticalLayout.addWidget(self.boton_clientes)

        self.boton_productos = QPushButton(self.widget_lateral)
        self.boton_productos.setObjectName(u"boton_productos")
        self.boton_productos.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.verticalLayout.addWidget(self.boton_productos)


        self.contenedor_widgets.addWidget(self.widget_lateral, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.stacked_widget = QStackedWidget(self.contenedor_principal)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.facturar = QWidget()
        self.facturar.setObjectName(u"facturar")
        self.verticalLayout_3 = QVBoxLayout(self.facturar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.NACIONALIDAD = QComboBox(self.facturar)
        self.NACIONALIDAD.addItem("")
        self.NACIONALIDAD.addItem("")
        self.NACIONALIDAD.addItem("")
        self.NACIONALIDAD.setObjectName(u"NACIONALIDAD")

        self.gridLayout.addWidget(self.NACIONALIDAD, 0, 0, 1, 1)

        self.NOMBRE = QLineEdit(self.facturar)
        self.NOMBRE.setObjectName(u"NOMBRE")
        self.NOMBRE.setEnabled(True)
        self.NOMBRE.setCursorPosition(0)
        self.NOMBRE.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.NOMBRE, 2, 1, 1, 1)

        self.EDITAR = QCheckBox(self.facturar)
        self.EDITAR.setObjectName(u"EDITAR")

        self.gridLayout.addWidget(self.EDITAR, 2, 0, 1, 1)

        self.APELLIDO = QLineEdit(self.facturar)
        self.APELLIDO.setObjectName(u"APELLIDO")
        self.APELLIDO.setCursorPosition(0)
        self.APELLIDO.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.APELLIDO, 2, 2, 1, 1)

        self.DIRECCION = QTextEdit(self.facturar)
        self.DIRECCION.setObjectName(u"DIRECCION")
        self.DIRECCION.setTabChangesFocus(True)

        self.gridLayout.addWidget(self.DIRECCION, 4, 1, 1, 2)

        self.TELEFONO = QLineEdit(self.facturar)
        self.TELEFONO.setObjectName(u"TELEFONO")
        self.TELEFONO.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.TELEFONO, 5, 1, 1, 2)

        self.REGISTRAR = QPushButton(self.facturar)
        self.REGISTRAR.setObjectName(u"REGISTRAR")

        self.gridLayout.addWidget(self.REGISTRAR, 6, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.CEDULA = QLineEdit(self.facturar)
        self.CEDULA.setObjectName(u"CEDULA")
        self.CEDULA.setCursorPosition(0)
        self.CEDULA.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.CEDULA, 0, 1, 1, 2)

        self.BUSCAR = QPushButton(self.facturar)
        self.BUSCAR.setObjectName(u"BUSCAR")
        self.BUSCAR.setEnabled(True)

        self.gridLayout.addWidget(self.BUSCAR, 1, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.stacked_widget.addWidget(self.facturar)
        self.clientes = QWidget()
        self.clientes.setObjectName(u"clientes")
        self.stacked_widget.addWidget(self.clientes)
        self.productos = QWidget()
        self.productos.setObjectName(u"productos")
        self.stacked_widget.addWidget(self.productos)

        self.contenedor_widgets.addWidget(self.stacked_widget, 1, 1, 1, 1)

        self.contenedor_widgets.setRowStretch(0, 1)
        self.contenedor_widgets.setRowStretch(1, 9)
        self.contenedor_widgets.setColumnStretch(0, 1)
        self.contenedor_widgets.setColumnStretch(1, 7)

        self.verticalLayout_2.addWidget(self.contenedor_principal)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.boton_cierre, self.boton_facturar)
        QWidget.setTabOrder(self.boton_facturar, self.boton_clientes)
        QWidget.setTabOrder(self.boton_clientes, self.boton_productos)
        QWidget.setTabOrder(self.boton_productos, self.NACIONALIDAD)
        QWidget.setTabOrder(self.NACIONALIDAD, self.CEDULA)
        QWidget.setTabOrder(self.CEDULA, self.BUSCAR)
        QWidget.setTabOrder(self.BUSCAR, self.EDITAR)
        QWidget.setTabOrder(self.EDITAR, self.NOMBRE)
        QWidget.setTabOrder(self.NOMBRE, self.APELLIDO)
        QWidget.setTabOrder(self.APELLIDO, self.DIRECCION)
        QWidget.setTabOrder(self.DIRECCION, self.TELEFONO)
        QWidget.setTabOrder(self.TELEFONO, self.REGISTRAR)
        QWidget.setTabOrder(self.REGISTRAR, self.boton_configuracion)
        QWidget.setTabOrder(self.boton_configuracion, self.boton_cerrar_sesion)

        self.retranslateUi(MainWindow)

        self.stacked_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.boton_cierre.setText(QCoreApplication.translate("MainWindow", u"CIERRE", None))
        self.boton_configuracion.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACI\u00d3N", None))
        self.boton_cerrar_sesion.setText(QCoreApplication.translate("MainWindow", u"CERRAR SESI\u00d3N", None))
        self.label.setText("")
        self.boton_facturar.setText(QCoreApplication.translate("MainWindow", u"FACTURAR", None))
        self.boton_clientes.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
        self.boton_productos.setText(QCoreApplication.translate("MainWindow", u"PRODUCTOS", None))
        self.NACIONALIDAD.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.NACIONALIDAD.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))
        self.NACIONALIDAD.setItemText(2, QCoreApplication.translate("MainWindow", u"J", None))

        self.NOMBRE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.EDITAR.setText(QCoreApplication.translate("MainWindow", u"EDITAR", None))
        self.APELLIDO.setPlaceholderText(QCoreApplication.translate("MainWindow", u"APELLIDO", None))
        self.DIRECCION.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DIRECCI\u00d3N", None))
        self.TELEFONO.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONO", None))
        self.REGISTRAR.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.CEDULA.setText("")
        self.CEDULA.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEDULA", None))
        self.BUSCAR.setText(QCoreApplication.translate("MainWindow", u"BUSCAR CLIENTE", None))
    # retranslateUi

