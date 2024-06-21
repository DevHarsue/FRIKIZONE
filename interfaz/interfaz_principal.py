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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDoubleSpinBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QStatusBar,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

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
"	background: rgba(0,0,0,220)\n"
"}\n"
"\n"
"#widget_lateral QPushButton, #widget_superior QPushButton{\n"
"	border: none;\n"
"	border-bottom: 1px solid white;\n"
"	width: 100%;\n"
"	padding: 1em 8px;\n"
"}\n"
"\n"
"#widget_superior QPushButton{\n"
"	border: none;\n"
"	border-right: 1px solid white;\n"
"}\n"
"\n"
"#widget_lateral QPushButton:hover, #widget_superior QPushButton:hover{\n"
"	border-color: rgb(0, 255, 255);\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"#widget_lateral QPushButton:pressed, #widget_superior QPushButton:pressed{\n"
"	border-color: rgb(17, 165, 237);\n"
"	color: rgb(17, 165, 237);\n"
"}\n"
"\n"
"#stacked_widget QWidget{\n"
"	background: rgba(0,0,0,200);\n"
"}\n"
"\n"
"QStatusBar{\n"
"	background: black;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.contenedor_principal = QWidget(self.centralwidget)
        self.contenedor_principal.setObjectName(u"contenedor_principal")
        self.contenedor_principal.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.contenedor_principal)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_superior = QWidget(self.contenedor_principal)
        self.widget_superior.setObjectName(u"widget_superior")
        self.horizontalLayout = QHBoxLayout(self.widget_superior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.boton_v_cierre = QPushButton(self.widget_superior)
        self.boton_v_cierre.setObjectName(u"boton_v_cierre")

        self.horizontalLayout.addWidget(self.boton_v_cierre)

        self.boton_v_configuracion = QPushButton(self.widget_superior)
        self.boton_v_configuracion.setObjectName(u"boton_v_configuracion")

        self.horizontalLayout.addWidget(self.boton_v_configuracion)

        self.boton_v_cerrar_sesion = QPushButton(self.widget_superior)
        self.boton_v_cerrar_sesion.setObjectName(u"boton_v_cerrar_sesion")
        self.boton_v_cerrar_sesion.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.boton_v_cerrar_sesion)


        self.gridLayout.addWidget(self.widget_superior, 0, 0, 1, 2, Qt.AlignmentFlag.AlignRight)

        self.contenedor_logo = QWidget(self.contenedor_principal)
        self.contenedor_logo.setObjectName(u"contenedor_logo")
        self.verticalLayout_4 = QVBoxLayout(self.contenedor_logo)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.contenedor_logo)
        self.logo.setObjectName(u"logo")
        self.logo.setEnabled(True)
        self.logo.setMaximumSize(QSize(120, 120))
        self.logo.setPixmap(QPixmap(u"../images/logo.png"))
        self.logo.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.logo, 0, Qt.AlignmentFlag.AlignRight)


        self.gridLayout.addWidget(self.contenedor_logo, 0, 2, 1, 1)

        self.widget_lateral = QWidget(self.contenedor_principal)
        self.widget_lateral.setObjectName(u"widget_lateral")
        self.verticalLayout = QVBoxLayout(self.widget_lateral)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 0, 8, 8)
        self.boton_v_facturar = QPushButton(self.widget_lateral)
        self.boton_v_facturar.setObjectName(u"boton_v_facturar")
        self.boton_v_facturar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.boton_v_facturar)

        self.boton_v_productos = QPushButton(self.widget_lateral)
        self.boton_v_productos.setObjectName(u"boton_v_productos")
        self.boton_v_productos.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_v_productos.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.verticalLayout.addWidget(self.boton_v_productos)

        self.boton_v_registrar_clientes = QPushButton(self.widget_lateral)
        self.boton_v_registrar_clientes.setObjectName(u"boton_v_registrar_clientes")
        self.boton_v_registrar_clientes.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.boton_v_registrar_clientes)

        self.boton_v_registar_productos = QPushButton(self.widget_lateral)
        self.boton_v_registar_productos.setObjectName(u"boton_v_registar_productos")
        self.boton_v_registar_productos.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.boton_v_registar_productos)


        self.gridLayout.addWidget(self.widget_lateral, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.stacked_widget = QStackedWidget(self.contenedor_principal)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.stacked_widget.setMinimumSize(QSize(0, 0))
        self.stacked_widget.setStyleSheet(u"QComboBox{\n"
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
"	background: black;\n"
"	border: none;\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0, 85, 255);	\n"
"	outline: none;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background: transparent;\n"
"	border: none;\n"
"	min-width: 10em;\n"
"	border-bottom: 1px solid white;\n"
"	padding: 0.6em 0.4em;\n"
"	color: rgb(0, 255, 255);\n"
"	font-size: 13px;\n"
"	selection-color: rgb(0, 255, 255);\n"
"	selection-background-color: rgba(0, 0, 0, 200);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image: url(\"images/lock.png\");\n"
"	width: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
""
                        "	image: url(\"images/unlock.png\");\n"
"	width: 25px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: none;\n"
"	padding: 0.2em 1em 0.2em 1em;\n"
"	background: transparent;\n"
"	border-bottom: 1px solid white;\n"
"	border-top: 1px solid white;\n"
"	min-width: 10em;\n"
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
"QTextEdit{\n"
"	font-size: 14px;\n"
"	background: transparent;\n"
"	color: rgb(0,255,255);\n"
"	border: none;\n"
"	border: 1px solid white;\n"
"	border-radius: 3px;\n"
"	selection-color: rgb(0, 255, 255);\n"
"	selection-background-color: rgba(0, 0, 0, 200);\n"
"}\n"
"\n"
"QTextEdit:focus{\n"
"	border-color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"	background: transparent;\n"
"	font-size: 13px;\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"QDoubleSpinBox, QSpinBox,QDateE"
                        "dit {\n"
"	min-width: 8em;\n"
"    padding-right: 25px; \n"
"	border: none;\n"
"    border-bottom: 1px solid white;\n"
"	background: transparent;\n"
"	selection-color: rgb(0, 255, 255);\n"
"	selection-background-color: rgba(0, 0, 0, 200);\n"
"}\n"
"\n"
"QDoubleSpinBox:focus,QSpinBox:focus,QDateEdit:focus {\n"
"	border-color: rgb(0, 255, 255);\n"
"	color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"QCalendarWidget{\n"
"	min-width:18em;\n"
"	font-size:14px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"    alternate-background-color: transparent;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth{\n"
"	qproperty-icon:url(\"images/left-arrow.png\");\n"
"}\n"
"\n"
"#qt_calendar_nextmonth{\n"
"	qproperty-icon:url(\"images/right-arrow.png\");\n"
"}\n"
"\n"
"#qt_calendar_navigationbar QSpinBox{\n"
"	min-width:4em;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"        border: 1px solid white;\n"
"        width:10px;\n"
"        margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
" ba"
                        "ckground: rgb(0, 255, 255);\n"
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
"}\n"
"\n"
"QTableView{\n"
"	background:transparent;\n"
"}\n"
"QTableView::item:selected{\n"
"	background:black;\n"
"	color:rgb(0, 255, 255);;\n"
"}\n"
"")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stacked_widget.addWidget(self.page_2)
        self.vista_registrar_clientes = QWidget()
        self.vista_registrar_clientes.setObjectName(u"vista_registrar_clientes")
        self.verticalLayout_3 = QVBoxLayout(self.vista_registrar_clientes)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.layout_registrar_clientes = QGridLayout()
        self.layout_registrar_clientes.setObjectName(u"layout_registrar_clientes")
        self.text_descripcion_rcliente = QTextEdit(self.vista_registrar_clientes)
        self.text_descripcion_rcliente.setObjectName(u"text_descripcion_rcliente")
        self.text_descripcion_rcliente.setTabChangesFocus(True)

        self.layout_registrar_clientes.addWidget(self.text_descripcion_rcliente, 6, 1, 1, 2)

        self.line_apellido_rcliente = QLineEdit(self.vista_registrar_clientes)
        self.line_apellido_rcliente.setObjectName(u"line_apellido_rcliente")
        self.line_apellido_rcliente.setCursorPosition(0)
        self.line_apellido_rcliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_registrar_clientes.addWidget(self.line_apellido_rcliente, 4, 2, 1, 1)

        self.check_editar_rcliente = QCheckBox(self.vista_registrar_clientes)
        self.check_editar_rcliente.setObjectName(u"check_editar_rcliente")
        self.check_editar_rcliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_registrar_clientes.addWidget(self.check_editar_rcliente, 4, 0, 1, 1)

        self.combo_nacionalidad_rcliente = QComboBox(self.vista_registrar_clientes)
        self.combo_nacionalidad_rcliente.addItem("")
        self.combo_nacionalidad_rcliente.addItem("")
        self.combo_nacionalidad_rcliente.setObjectName(u"combo_nacionalidad_rcliente")
        self.combo_nacionalidad_rcliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_registrar_clientes.addWidget(self.combo_nacionalidad_rcliente, 0, 0, 1, 1)

        self.boton_buscar_rcliente = QPushButton(self.vista_registrar_clientes)
        self.boton_buscar_rcliente.setObjectName(u"boton_buscar_rcliente")
        self.boton_buscar_rcliente.setEnabled(True)
        self.boton_buscar_rcliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_registrar_clientes.addWidget(self.boton_buscar_rcliente, 1, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.line_nombre_rcliente = QLineEdit(self.vista_registrar_clientes)
        self.line_nombre_rcliente.setObjectName(u"line_nombre_rcliente")
        self.line_nombre_rcliente.setEnabled(True)
        self.line_nombre_rcliente.setCursorPosition(0)
        self.line_nombre_rcliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_registrar_clientes.addWidget(self.line_nombre_rcliente, 4, 1, 1, 1)

        self.line_cedula_rcliente = QLineEdit(self.vista_registrar_clientes)
        self.line_cedula_rcliente.setObjectName(u"line_cedula_rcliente")
        self.line_cedula_rcliente.setCursorPosition(0)
        self.line_cedula_rcliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_registrar_clientes.addWidget(self.line_cedula_rcliente, 0, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.line_telefono_rcliente = QLineEdit(self.vista_registrar_clientes)
        self.line_telefono_rcliente.setObjectName(u"line_telefono_rcliente")
        self.line_telefono_rcliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_registrar_clientes.addWidget(self.line_telefono_rcliente, 7, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.boton_registrar_rcliente = QPushButton(self.vista_registrar_clientes)
        self.boton_registrar_rcliente.setObjectName(u"boton_registrar_rcliente")
        self.boton_registrar_rcliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_registrar_clientes.addWidget(self.boton_registrar_rcliente, 8, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_3.addLayout(self.layout_registrar_clientes)

        self.stacked_widget.addWidget(self.vista_registrar_clientes)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stacked_widget.addWidget(self.page)
        self.vista_facturar = QWidget()
        self.vista_facturar.setObjectName(u"vista_facturar")
        self.verticalLayout_13 = QVBoxLayout(self.vista_facturar)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.boton_buscar_producto_facturar = QPushButton(self.vista_facturar)
        self.boton_buscar_producto_facturar.setObjectName(u"boton_buscar_producto_facturar")

        self.gridLayout_4.addWidget(self.boton_buscar_producto_facturar, 2, 1, 1, 1)

        self.line_cedula_facturar = QLineEdit(self.vista_facturar)
        self.line_cedula_facturar.setObjectName(u"line_cedula_facturar")

        self.gridLayout_4.addWidget(self.line_cedula_facturar, 0, 1, 1, 1)

        self.boton_buscar_cliente_facturar = QPushButton(self.vista_facturar)
        self.boton_buscar_cliente_facturar.setObjectName(u"boton_buscar_cliente_facturar")
        icon = QIcon(QIcon.fromTheme(u"system-search"))
        self.boton_buscar_cliente_facturar.setIcon(icon)

        self.gridLayout_4.addWidget(self.boton_buscar_cliente_facturar, 0, 2, 1, 1, Qt.AlignmentFlag.AlignBottom)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_bs_facturar = QLabel(self.vista_facturar)
        self.label_bs_facturar.setObjectName(u"label_bs_facturar")

        self.gridLayout_5.addWidget(self.label_bs_facturar, 1, 1, 1, 1)

        self.double_dolares_facturar = QDoubleSpinBox(self.vista_facturar)
        self.double_dolares_facturar.setObjectName(u"double_dolares_facturar")

        self.gridLayout_5.addWidget(self.double_dolares_facturar, 0, 0, 1, 1)

        self.label_dolar_facturar = QLabel(self.vista_facturar)
        self.label_dolar_facturar.setObjectName(u"label_dolar_facturar")

        self.gridLayout_5.addWidget(self.label_dolar_facturar, 1, 0, 1, 1)

        self.label_cop_facturar = QLabel(self.vista_facturar)
        self.label_cop_facturar.setObjectName(u"label_cop_facturar")

        self.gridLayout_5.addWidget(self.label_cop_facturar, 1, 2, 1, 1)

        self.double_bs_facturar = QDoubleSpinBox(self.vista_facturar)
        self.double_bs_facturar.setObjectName(u"double_bs_facturar")

        self.gridLayout_5.addWidget(self.double_bs_facturar, 0, 1, 1, 1)

        self.spin_cop_facturar = QSpinBox(self.vista_facturar)
        self.spin_cop_facturar.setObjectName(u"spin_cop_facturar")
        self.spin_cop_facturar.setMinimum(0)
        self.spin_cop_facturar.setMaximum(100000000)
        self.spin_cop_facturar.setSingleStep(1000)
        self.spin_cop_facturar.setDisplayIntegerBase(10)

        self.gridLayout_5.addWidget(self.spin_cop_facturar, 0, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_5, 5, 0, 1, 3)

        self.boton_facturar = QPushButton(self.vista_facturar)
        self.boton_facturar.setObjectName(u"boton_facturar")

        self.gridLayout_4.addWidget(self.boton_facturar, 6, 1, 1, 1)

        self.line_nombre_facturar = QLineEdit(self.vista_facturar)
        self.line_nombre_facturar.setObjectName(u"line_nombre_facturar")
        self.line_nombre_facturar.setEnabled(False)

        self.gridLayout_4.addWidget(self.line_nombre_facturar, 1, 0, 1, 1)

        self.combo_nacionalidad_facturar = QComboBox(self.vista_facturar)
        self.combo_nacionalidad_facturar.addItem("")
        self.combo_nacionalidad_facturar.addItem("")
        self.combo_nacionalidad_facturar.setObjectName(u"combo_nacionalidad_facturar")

        self.gridLayout_4.addWidget(self.combo_nacionalidad_facturar, 0, 0, 1, 1)

        self.line_apellido_facturar = QLineEdit(self.vista_facturar)
        self.line_apellido_facturar.setObjectName(u"line_apellido_facturar")
        self.line_apellido_facturar.setEnabled(False)

        self.gridLayout_4.addWidget(self.line_apellido_facturar, 1, 2, 1, 1)

        self.label_total = QLabel(self.vista_facturar)
        self.label_total.setObjectName(u"label_total")

        self.gridLayout_4.addWidget(self.label_total, 4, 0, 1, 2)

        self.list_productos_facturar = QListWidget(self.vista_facturar)
        self.list_productos_facturar.setObjectName(u"list_productos_facturar")

        self.gridLayout_4.addWidget(self.list_productos_facturar, 3, 0, 1, 3)


        self.verticalLayout_13.addLayout(self.gridLayout_4)

        self.stacked_widget.addWidget(self.vista_facturar)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stacked_widget.addWidget(self.page_4)
        self.vista_productos = QWidget()
        self.vista_productos.setObjectName(u"vista_productos")
        self.verticalLayout_9 = QVBoxLayout(self.vista_productos)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_bproducto = QLineEdit(self.vista_productos)
        self.line_bproducto.setObjectName(u"line_bproducto")
        self.line_bproducto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.line_bproducto, 0, 1, 1, 1)

        self.combo_buscar_bproducto = QComboBox(self.vista_productos)
        self.combo_buscar_bproducto.addItem("")
        self.combo_buscar_bproducto.addItem("")
        self.combo_buscar_bproducto.addItem("")
        self.combo_buscar_bproducto.setObjectName(u"combo_buscar_bproducto")
        self.combo_buscar_bproducto.setMinimumSize(QSize(64, 0))
        self.combo_buscar_bproducto.setStyleSheet(u"min-width: 4em;")

        self.gridLayout_2.addWidget(self.combo_buscar_bproducto, 0, 0, 1, 1)

        self.boton_buscar_bproducto = QPushButton(self.vista_productos)
        self.boton_buscar_bproducto.setObjectName(u"boton_buscar_bproducto")
        self.boton_buscar_bproducto.setIcon(icon)

        self.gridLayout_2.addWidget(self.boton_buscar_bproducto, 0, 2, 1, 1)

        self.list_productos = QTableWidget(self.vista_productos)
        if (self.list_productos.columnCount() < 5):
            self.list_productos.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.list_productos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.list_productos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.list_productos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.list_productos.setObjectName(u"list_productos")
        self.list_productos.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_productos.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list_productos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.list_productos.setShowGrid(False)
        self.list_productos.setRowCount(0)
        self.list_productos.horizontalHeader().setCascadingSectionResizes(False)
        self.list_productos.horizontalHeader().setDefaultSectionSize(192)
        self.list_productos.horizontalHeader().setProperty("showSortIndicator", False)
        self.list_productos.horizontalHeader().setStretchLastSection(True)
        self.list_productos.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.list_productos, 1, 0, 1, 3)


        self.verticalLayout_9.addLayout(self.gridLayout_2)

        self.stacked_widget.addWidget(self.vista_productos)
        self.vista_cierre = QWidget()
        self.vista_cierre.setObjectName(u"vista_cierre")
        self.verticalLayout_7 = QVBoxLayout(self.vista_cierre)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.date_cierre = QDateEdit(self.vista_cierre)
        self.date_cierre.setObjectName(u"date_cierre")
        self.date_cierre.setCalendarPopup(True)
        self.date_cierre.setDate(QDate(2024, 1, 1))

        self.gridLayout_6.addWidget(self.date_cierre, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.total_dolares_cierre = QLabel(self.vista_cierre)
        self.total_dolares_cierre.setObjectName(u"total_dolares_cierre")

        self.gridLayout_6.addWidget(self.total_dolares_cierre, 5, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.vista_cierre)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_6.addWidget(self.pushButton_3, 8, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_total_dolares_cierre = QLabel(self.vista_cierre)
        self.label_total_dolares_cierre.setObjectName(u"label_total_dolares_cierre")

        self.gridLayout_6.addWidget(self.label_total_dolares_cierre, 6, 0, 1, 1)

        self.pushButton = QPushButton(self.vista_cierre)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_6.addWidget(self.pushButton, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.total_cop_cierre = QLabel(self.vista_cierre)
        self.total_cop_cierre.setObjectName(u"total_cop_cierre")

        self.gridLayout_6.addWidget(self.total_cop_cierre, 7, 0, 1, 1)

        self.label_tasa_cop_cierre = QLabel(self.vista_cierre)
        self.label_tasa_cop_cierre.setObjectName(u"label_tasa_cop_cierre")

        self.gridLayout_6.addWidget(self.label_tasa_cop_cierre, 3, 0, 1, 1)

        self.tasa_bcv_cierre = QLabel(self.vista_cierre)
        self.tasa_bcv_cierre.setObjectName(u"tasa_bcv_cierre")

        self.gridLayout_6.addWidget(self.tasa_bcv_cierre, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 4, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_6)

        self.stacked_widget.addWidget(self.vista_cierre)
        self.vista_configuracion = QWidget()
        self.vista_configuracion.setObjectName(u"vista_configuracion")
        self.verticalLayout_11 = QVBoxLayout(self.vista_configuracion)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_2 = QPushButton(self.vista_configuracion)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_5.addWidget(self.pushButton_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.contenedor_configs_bd = QWidget(self.vista_configuracion)
        self.contenedor_configs_bd.setObjectName(u"contenedor_configs_bd")
        self.verticalLayout_8 = QVBoxLayout(self.contenedor_configs_bd)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.checkBox = QCheckBox(self.contenedor_configs_bd)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)
        self.checkBox.setChecked(True)

        self.verticalLayout_8.addWidget(self.checkBox)

        self.lineEdit = QLineEdit(self.contenedor_configs_bd)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)

        self.verticalLayout_8.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.contenedor_configs_bd)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)

        self.verticalLayout_8.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.contenedor_configs_bd)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(False)

        self.verticalLayout_8.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.contenedor_configs_bd)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(False)

        self.verticalLayout_8.addWidget(self.lineEdit_4)

        self.pushButton_4 = QPushButton(self.contenedor_configs_bd)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)

        self.verticalLayout_8.addWidget(self.pushButton_4, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_5.addWidget(self.contenedor_configs_bd)


        self.verticalLayout_11.addLayout(self.verticalLayout_5)

        self.stacked_widget.addWidget(self.vista_configuracion)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stacked_widget.addWidget(self.page_3)
        self.vista_registrar_productos = QWidget()
        self.vista_registrar_productos.setObjectName(u"vista_registrar_productos")
        self.verticalLayout_6 = QVBoxLayout(self.vista_registrar_productos)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(16, 16, 16, 16)
        self.layout_registrar_productos = QVBoxLayout()
        self.layout_registrar_productos.setObjectName(u"layout_registrar_productos")
        self.layout_registrar_productos.setContentsMargins(8, -1, 8, -1)
        self.line_nombre_rproducto = QLineEdit(self.vista_registrar_productos)
        self.line_nombre_rproducto.setObjectName(u"line_nombre_rproducto")
        self.line_nombre_rproducto.setMinimumSize(QSize(184, 0))
        self.line_nombre_rproducto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_registrar_productos.addWidget(self.line_nombre_rproducto, 0, Qt.AlignmentFlag.AlignHCenter)

        self.text_descripcion_rproducto = QTextEdit(self.vista_registrar_productos)
        self.text_descripcion_rproducto.setObjectName(u"text_descripcion_rproducto")
        self.text_descripcion_rproducto.setTabChangesFocus(True)

        self.layout_registrar_productos.addWidget(self.text_descripcion_rproducto)

        self.label_precio = QLabel(self.vista_registrar_productos)
        self.label_precio.setObjectName(u"label_precio")
        self.label_precio.setMinimumSize(QSize(200, 0))
        self.label_precio.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_registrar_productos.addWidget(self.label_precio)

        self.double_precio_rproducto = QDoubleSpinBox(self.vista_registrar_productos)
        self.double_precio_rproducto.setObjectName(u"double_precio_rproducto")
        self.double_precio_rproducto.setCursor(QCursor(Qt.ArrowCursor))
        self.double_precio_rproducto.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.layout_registrar_productos.addWidget(self.double_precio_rproducto, 0, Qt.AlignmentFlag.AlignHCenter)

        self.boton_registrar_rproducto = QPushButton(self.vista_registrar_productos)
        self.boton_registrar_rproducto.setObjectName(u"boton_registrar_rproducto")
        self.boton_registrar_rproducto.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_registrar_productos.addWidget(self.boton_registrar_rproducto, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_6.addLayout(self.layout_registrar_productos)

        self.stacked_widget.addWidget(self.vista_registrar_productos)

        self.gridLayout.addWidget(self.stacked_widget, 1, 1, 1, 2)

        self.gridLayout.setColumnStretch(2, 1)

        self.verticalLayout_2.addWidget(self.contenedor_principal)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.boton_v_facturar, self.boton_v_productos)
        QWidget.setTabOrder(self.boton_v_productos, self.line_nombre_rproducto)
        QWidget.setTabOrder(self.line_nombre_rproducto, self.text_descripcion_rproducto)
        QWidget.setTabOrder(self.text_descripcion_rproducto, self.double_precio_rproducto)
        QWidget.setTabOrder(self.double_precio_rproducto, self.boton_registrar_rproducto)
        QWidget.setTabOrder(self.boton_registrar_rproducto, self.boton_v_configuracion)
        QWidget.setTabOrder(self.boton_v_configuracion, self.line_telefono_rcliente)
        QWidget.setTabOrder(self.line_telefono_rcliente, self.boton_registrar_rcliente)
        QWidget.setTabOrder(self.boton_registrar_rcliente, self.combo_nacionalidad_rcliente)
        QWidget.setTabOrder(self.combo_nacionalidad_rcliente, self.line_cedula_rcliente)
        QWidget.setTabOrder(self.line_cedula_rcliente, self.boton_buscar_rcliente)
        QWidget.setTabOrder(self.boton_buscar_rcliente, self.check_editar_rcliente)
        QWidget.setTabOrder(self.check_editar_rcliente, self.text_descripcion_rcliente)
        QWidget.setTabOrder(self.text_descripcion_rcliente, self.line_apellido_rcliente)
        QWidget.setTabOrder(self.line_apellido_rcliente, self.line_nombre_rcliente)

        self.retranslateUi(MainWindow)

        self.stacked_widget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.boton_v_cierre.setText(QCoreApplication.translate("MainWindow", u"CIERRE", None))
        self.boton_v_configuracion.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACI\u00d3N", None))
        self.boton_v_cerrar_sesion.setText(QCoreApplication.translate("MainWindow", u"CERRAR SESI\u00d3N", None))
        self.logo.setText("")
        self.boton_v_facturar.setText(QCoreApplication.translate("MainWindow", u"FACTURAR", None))
        self.boton_v_productos.setText(QCoreApplication.translate("MainWindow", u"PRODUCTOS", None))
        self.boton_v_registrar_clientes.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR\n"
"CLIENTES", None))
        self.boton_v_registar_productos.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR\n"
"PRODUCTOS", None))
        self.text_descripcion_rcliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DIRECCI\u00d3N (OPCIONAL)", None))
        self.line_apellido_rcliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"APELLIDO", None))
        self.check_editar_rcliente.setText(QCoreApplication.translate("MainWindow", u"EDITAR", None))
        self.combo_nacionalidad_rcliente.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.combo_nacionalidad_rcliente.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))

        self.boton_buscar_rcliente.setText(QCoreApplication.translate("MainWindow", u"BUSCAR CLIENTE CNE", None))
        self.line_nombre_rcliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.line_cedula_rcliente.setText("")
        self.line_cedula_rcliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEDULA", None))
        self.line_telefono_rcliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONO", None))
        self.boton_registrar_rcliente.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.boton_buscar_producto_facturar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR PRODUCTO", None))
        self.line_cedula_facturar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEDULA", None))
        self.boton_buscar_cliente_facturar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.label_bs_facturar.setText(QCoreApplication.translate("MainWindow", u"Valor BS:", None))
        self.label_dolar_facturar.setText(QCoreApplication.translate("MainWindow", u"Valor $:", None))
        self.label_cop_facturar.setText(QCoreApplication.translate("MainWindow", u"Valor COP:", None))
        self.boton_facturar.setText(QCoreApplication.translate("MainWindow", u"FACTURAR", None))
        self.line_nombre_facturar.setText("")
        self.line_nombre_facturar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.combo_nacionalidad_facturar.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.combo_nacionalidad_facturar.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))

        self.line_apellido_facturar.setText("")
        self.line_apellido_facturar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"APELLIDO", None))
        self.label_total.setText(QCoreApplication.translate("MainWindow", u"TOTAL EN DOLARES:", None))
        self.line_bproducto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.combo_buscar_bproducto.setItemText(0, QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.combo_buscar_bproducto.setItemText(1, QCoreApplication.translate("MainWindow", u"PRECIO", None))
        self.combo_buscar_bproducto.setItemText(2, QCoreApplication.translate("MainWindow", u"ID", None))

        self.boton_buscar_bproducto.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        ___qtablewidgetitem = self.list_productos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None));
        ___qtablewidgetitem1 = self.list_productos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"DESCRIPCI\u00d3N", None));
        ___qtablewidgetitem2 = self.list_productos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None));
        self.total_dolares_cierre.setText(QCoreApplication.translate("MainWindow", u"TOTAL BS:", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"IMPRIMIR", None))
        self.label_total_dolares_cierre.setText(QCoreApplication.translate("MainWindow", u"TOTAL DOLARES:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"GENERAR", None))
        self.total_cop_cierre.setText(QCoreApplication.translate("MainWindow", u"TOTAL COP:", None))
        self.label_tasa_cop_cierre.setText(QCoreApplication.translate("MainWindow", u"TASA COP:", None))
        self.tasa_bcv_cierre.setText(QCoreApplication.translate("MainWindow", u"TASA BCV:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"CAMBIAR USUARIOS", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CAMBIAR CONFIGURACIONES DE LA BASE DE DATOS", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"USUARIO", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CONTRASE\u00d1A", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HOST", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PUERTO", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"ACEPTAR", None))
        self.line_nombre_rproducto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE PRODUCTO", None))
        self.text_descripcion_rproducto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DESCRIPCI\u00d3N DEL PRODUCTO (OPCIONAL)", None))
        self.label_precio.setText(QCoreApplication.translate("MainWindow", u"PRECI\u00d3 EN DOLARES:", None))
        self.boton_registrar_rproducto.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
    # retranslateUi
