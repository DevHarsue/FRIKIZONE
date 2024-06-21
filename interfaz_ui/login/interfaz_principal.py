# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_principalXqTFgx.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDoubleSpinBox, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainPrincipal(object):
    def setupUi(self, MainPrincipal):
        if not MainPrincipal.objectName():
            MainPrincipal.setObjectName(u"MainPrincipal")
        MainPrincipal.resize(800, 600)
        MainPrincipal.setMinimumSize(QSize(800, 600))
        MainPrincipal.setStyleSheet(u"*{\n"
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
        self.centralwidget = QWidget(MainPrincipal)
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
        self.logo.setPixmap(QPixmap(u"../../images/logo.png"))
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

        self.boton_v_clientes = QPushButton(self.widget_lateral)
        self.boton_v_clientes.setObjectName(u"boton_v_clientes")
        self.boton_v_clientes.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.boton_v_clientes)

        self.boton_v_productos = QPushButton(self.widget_lateral)
        self.boton_v_productos.setObjectName(u"boton_v_productos")
        self.boton_v_productos.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_v_productos.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.verticalLayout.addWidget(self.boton_v_productos)

        self.boton_v_registrar = QPushButton(self.widget_lateral)
        self.boton_v_registrar.setObjectName(u"boton_v_registrar")

        self.verticalLayout.addWidget(self.boton_v_registrar)


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
"QListWidget{\n"
"	background: transparent;\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QListWidget:focus{\n"
"	border-color: rgb(0, 255, 255);\n"
"}\n"
"\n"
"")
        self.vista_registros = QWidget()
        self.vista_registros.setObjectName(u"vista_registros")
        self.verticalLayout_5 = QVBoxLayout(self.vista_registros)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.boton_v_registrar_clientes = QPushButton(self.vista_registros)
        self.boton_v_registrar_clientes.setObjectName(u"boton_v_registrar_clientes")
        self.boton_v_registrar_clientes.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.boton_v_registrar_clientes, 0, Qt.AlignmentFlag.AlignHCenter)

        self.boton_v_registar_productos = QPushButton(self.vista_registros)
        self.boton_v_registar_productos.setObjectName(u"boton_v_registar_productos")
        self.boton_v_registar_productos.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.boton_v_registar_productos, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.stacked_widget.addWidget(self.vista_registros)
        self.vista_registrar_clientes = QWidget()
        self.vista_registrar_clientes.setObjectName(u"vista_registrar_clientes")
        self.verticalLayout_3 = QVBoxLayout(self.vista_registrar_clientes)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.layout_registrar_clientes = QGridLayout()
        self.layout_registrar_clientes.setObjectName(u"layout_registrar_clientes")
        self.line_telefono_rcliente = QLineEdit(self.vista_registrar_clientes)
        self.line_telefono_rcliente.setObjectName(u"line_telefono_rcliente")
        self.line_telefono_rcliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_registrar_clientes.addWidget(self.line_telefono_rcliente, 5, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.line_nombre_rcliente = QLineEdit(self.vista_registrar_clientes)
        self.line_nombre_rcliente.setObjectName(u"line_nombre_rcliente")
        self.line_nombre_rcliente.setEnabled(True)
        self.line_nombre_rcliente.setCursorPosition(0)
        self.line_nombre_rcliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_registrar_clientes.addWidget(self.line_nombre_rcliente, 2, 1, 1, 1)

        self.combo_nacionalidad_rcliente = QComboBox(self.vista_registrar_clientes)
        self.combo_nacionalidad_rcliente.addItem("")
        self.combo_nacionalidad_rcliente.addItem("")
        self.combo_nacionalidad_rcliente.addItem("")
        self.combo_nacionalidad_rcliente.setObjectName(u"combo_nacionalidad_rcliente")
        self.combo_nacionalidad_rcliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_registrar_clientes.addWidget(self.combo_nacionalidad_rcliente, 0, 0, 1, 1)

        self.line_cedula_rcliente = QLineEdit(self.vista_registrar_clientes)
        self.line_cedula_rcliente.setObjectName(u"line_cedula_rcliente")
        self.line_cedula_rcliente.setCursorPosition(0)
        self.line_cedula_rcliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_registrar_clientes.addWidget(self.line_cedula_rcliente, 0, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.boton_buscar_rcliente = QPushButton(self.vista_registrar_clientes)
        self.boton_buscar_rcliente.setObjectName(u"boton_buscar_rcliente")
        self.boton_buscar_rcliente.setEnabled(True)
        self.boton_buscar_rcliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_registrar_clientes.addWidget(self.boton_buscar_rcliente, 1, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.text_descripcion_rcliente = QTextEdit(self.vista_registrar_clientes)
        self.text_descripcion_rcliente.setObjectName(u"text_descripcion_rcliente")
        self.text_descripcion_rcliente.setTabChangesFocus(True)

        self.layout_registrar_clientes.addWidget(self.text_descripcion_rcliente, 4, 1, 1, 2)

        self.check_editar_rcliente = QCheckBox(self.vista_registrar_clientes)
        self.check_editar_rcliente.setObjectName(u"check_editar_rcliente")
        self.check_editar_rcliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_registrar_clientes.addWidget(self.check_editar_rcliente, 2, 0, 1, 1)

        self.line_apellido_rcliente = QLineEdit(self.vista_registrar_clientes)
        self.line_apellido_rcliente.setObjectName(u"line_apellido_rcliente")
        self.line_apellido_rcliente.setCursorPosition(0)
        self.line_apellido_rcliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_registrar_clientes.addWidget(self.line_apellido_rcliente, 2, 2, 1, 1)

        self.boton_registrar_rcliente = QPushButton(self.vista_registrar_clientes)
        self.boton_registrar_rcliente.setObjectName(u"boton_registrar_rcliente")
        self.boton_registrar_rcliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_registrar_clientes.addWidget(self.boton_registrar_rcliente, 6, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)


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

        self.gridLayout_4.addWidget(self.line_nombre_facturar, 1, 0, 1, 1)

        self.combo_nacionalidad_facturar = QComboBox(self.vista_facturar)
        self.combo_nacionalidad_facturar.addItem("")
        self.combo_nacionalidad_facturar.addItem("")
        self.combo_nacionalidad_facturar.setObjectName(u"combo_nacionalidad_facturar")

        self.gridLayout_4.addWidget(self.combo_nacionalidad_facturar, 0, 0, 1, 1)

        self.line_apellido_facturar = QLineEdit(self.vista_facturar)
        self.line_apellido_facturar.setObjectName(u"line_apellido_facturar")

        self.gridLayout_4.addWidget(self.line_apellido_facturar, 1, 2, 1, 1)

        self.label_total = QLabel(self.vista_facturar)
        self.label_total.setObjectName(u"label_total")

        self.gridLayout_4.addWidget(self.label_total, 4, 0, 1, 2)

        self.list_productos_facturar = QListWidget(self.vista_facturar)
        self.list_productos_facturar.setObjectName(u"list_productos_facturar")

        self.gridLayout_4.addWidget(self.list_productos_facturar, 3, 0, 1, 3)


        self.verticalLayout_13.addLayout(self.gridLayout_4)

        self.stacked_widget.addWidget(self.vista_facturar)
        self.vista_clientes = QWidget()
        self.vista_clientes.setObjectName(u"vista_clientes")
        self.verticalLayout_10 = QVBoxLayout(self.vista_clientes)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line_bclientes = QLineEdit(self.vista_clientes)
        self.line_bclientes.setObjectName(u"line_bclientes")
        self.line_bclientes.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.line_bclientes, 0, 1, 1, 1)

        self.boton_buscar_bclientes = QPushButton(self.vista_clientes)
        self.boton_buscar_bclientes.setObjectName(u"boton_buscar_bclientes")
        self.boton_buscar_bclientes.setIcon(icon)

        self.gridLayout_3.addWidget(self.boton_buscar_bclientes, 0, 2, 1, 1)

        self.combo_buscar_bclientes = QComboBox(self.vista_clientes)
        self.combo_buscar_bclientes.addItem("")
        self.combo_buscar_bclientes.addItem("")
        self.combo_buscar_bclientes.addItem("")
        self.combo_buscar_bclientes.setObjectName(u"combo_buscar_bclientes")
        self.combo_buscar_bclientes.setMinimumSize(QSize(64, 0))
        self.combo_buscar_bclientes.setStyleSheet(u"min-width: 4em;")

        self.gridLayout_3.addWidget(self.combo_buscar_bclientes, 0, 0, 1, 1)

        self.list_clientes = QListWidget(self.vista_clientes)
        self.list_clientes.setObjectName(u"list_clientes")

        self.gridLayout_3.addWidget(self.list_clientes, 1, 0, 1, 3)


        self.verticalLayout_10.addLayout(self.gridLayout_3)

        self.stacked_widget.addWidget(self.vista_clientes)
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

        self.boton_buscar_bproducto = QPushButton(self.vista_productos)
        self.boton_buscar_bproducto.setObjectName(u"boton_buscar_bproducto")
        self.boton_buscar_bproducto.setIcon(icon)

        self.gridLayout_2.addWidget(self.boton_buscar_bproducto, 0, 2, 1, 1)

        self.combo_buscar_bproducto = QComboBox(self.vista_productos)
        self.combo_buscar_bproducto.addItem("")
        self.combo_buscar_bproducto.addItem("")
        self.combo_buscar_bproducto.addItem("")
        self.combo_buscar_bproducto.setObjectName(u"combo_buscar_bproducto")
        self.combo_buscar_bproducto.setMinimumSize(QSize(64, 0))
        self.combo_buscar_bproducto.setStyleSheet(u"min-width: 4em;")

        self.gridLayout_2.addWidget(self.combo_buscar_bproducto, 0, 0, 1, 1)

        self.list_productos = QListWidget(self.vista_productos)
        self.list_productos.setObjectName(u"list_productos")

        self.gridLayout_2.addWidget(self.list_productos, 1, 0, 1, 3)


        self.verticalLayout_9.addLayout(self.gridLayout_2)

        self.stacked_widget.addWidget(self.vista_productos)
        self.vista_cierre = QWidget()
        self.vista_cierre.setObjectName(u"vista_cierre")
        self.verticalLayout_7 = QVBoxLayout(self.vista_cierre)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, -1, -1, 20)
        self.cop_cierre = QLabel(self.vista_cierre)
        self.cop_cierre.setObjectName(u"cop_cierre")

        self.gridLayout_6.addWidget(self.cop_cierre, 4, 1, 1, 1)

        self.total_dolares_cierre = QLabel(self.vista_cierre)
        self.total_dolares_cierre.setObjectName(u"total_dolares_cierre")

        self.gridLayout_6.addWidget(self.total_dolares_cierre, 5, 0, 1, 1)

        self.label_tasa_cop_cierre = QLabel(self.vista_cierre)
        self.label_tasa_cop_cierre.setObjectName(u"label_tasa_cop_cierre")

        self.gridLayout_6.addWidget(self.label_tasa_cop_cierre, 1, 1, 1, 1)

        self.tasa_bcv_cierre = QLabel(self.vista_cierre)
        self.tasa_bcv_cierre.setObjectName(u"tasa_bcv_cierre")

        self.gridLayout_6.addWidget(self.tasa_bcv_cierre, 1, 0, 1, 1)

        self.bs_cierre = QLabel(self.vista_cierre)
        self.bs_cierre.setObjectName(u"bs_cierre")

        self.gridLayout_6.addWidget(self.bs_cierre, 5, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.vista_cierre)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_6.addWidget(self.pushButton_3, 6, 0, 1, 1)

        self.total_cop_cierre = QLabel(self.vista_cierre)
        self.total_cop_cierre.setObjectName(u"total_cop_cierre")

        self.gridLayout_6.addWidget(self.total_cop_cierre, 4, 0, 1, 1)

        self.date_cierre = QDateEdit(self.vista_cierre)
        self.date_cierre.setObjectName(u"date_cierre")
        self.date_cierre.setCalendarPopup(True)
        self.date_cierre.setDate(QDate(2024, 1, 1))

        self.gridLayout_6.addWidget(self.date_cierre, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.vista_cierre)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_6.addWidget(self.pushButton_4, 6, 1, 1, 1)

        self.dolares_cierre = QLabel(self.vista_cierre)
        self.dolares_cierre.setObjectName(u"dolares_cierre")

        self.gridLayout_6.addWidget(self.dolares_cierre, 3, 1, 1, 1)

        self.label_total_dolares_cierre = QLabel(self.vista_cierre)
        self.label_total_dolares_cierre.setObjectName(u"label_total_dolares_cierre")

        self.gridLayout_6.addWidget(self.label_total_dolares_cierre, 3, 0, 1, 1)

        self.pushButton = QPushButton(self.vista_cierre)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_6.addWidget(self.pushButton, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.gridLayout_6.setRowStretch(0, 1)
        self.gridLayout_6.setRowStretch(1, 1)
        self.gridLayout_6.setRowStretch(2, 4)
        self.gridLayout_6.setRowStretch(3, 1)
        self.gridLayout_6.setRowStretch(4, 1)
        self.gridLayout_6.setRowStretch(5, 1)
        self.gridLayout_6.setRowStretch(6, 1)

        self.verticalLayout_7.addLayout(self.gridLayout_6)

        self.stacked_widget.addWidget(self.vista_cierre)
        self.vista_configuracion = QWidget()
        self.vista_configuracion.setObjectName(u"vista_configuracion")
        self.verticalLayout_11 = QVBoxLayout(self.vista_configuracion)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_2 = QLabel(self.vista_configuracion)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_11.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stacked_widget.addWidget(self.vista_configuracion)
        self.vista_cerrar_sesion = QWidget()
        self.vista_cerrar_sesion.setObjectName(u"vista_cerrar_sesion")
        self.verticalLayout_12 = QVBoxLayout(self.vista_cerrar_sesion)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_3 = QLabel(self.vista_cerrar_sesion)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_12.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stacked_widget.addWidget(self.vista_cerrar_sesion)
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

        MainPrincipal.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        MainPrincipal.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.boton_v_facturar, self.boton_v_clientes)
        QWidget.setTabOrder(self.boton_v_clientes, self.boton_v_productos)
        QWidget.setTabOrder(self.boton_v_productos, self.line_nombre_rproducto)
        QWidget.setTabOrder(self.line_nombre_rproducto, self.text_descripcion_rproducto)
        QWidget.setTabOrder(self.text_descripcion_rproducto, self.double_precio_rproducto)
        QWidget.setTabOrder(self.double_precio_rproducto, self.boton_registrar_rproducto)
        QWidget.setTabOrder(self.boton_registrar_rproducto, self.boton_v_configuracion)
        QWidget.setTabOrder(self.boton_v_configuracion, self.line_telefono_rcliente)
        QWidget.setTabOrder(self.line_telefono_rcliente, self.boton_registrar_rcliente)
        QWidget.setTabOrder(self.boton_registrar_rcliente, self.boton_v_registrar_clientes)
        QWidget.setTabOrder(self.boton_v_registrar_clientes, self.combo_nacionalidad_rcliente)
        QWidget.setTabOrder(self.combo_nacionalidad_rcliente, self.line_cedula_rcliente)
        QWidget.setTabOrder(self.line_cedula_rcliente, self.boton_buscar_rcliente)
        QWidget.setTabOrder(self.boton_buscar_rcliente, self.check_editar_rcliente)
        QWidget.setTabOrder(self.check_editar_rcliente, self.boton_v_registar_productos)
        QWidget.setTabOrder(self.boton_v_registar_productos, self.text_descripcion_rcliente)
        QWidget.setTabOrder(self.text_descripcion_rcliente, self.line_apellido_rcliente)
        QWidget.setTabOrder(self.line_apellido_rcliente, self.line_nombre_rcliente)

        self.retranslateUi(MainPrincipal)

        self.stacked_widget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainPrincipal)
    # setupUi

    def retranslateUi(self, MainPrincipal):
        MainPrincipal.setWindowTitle(QCoreApplication.translate("MainPrincipal", u"MainWindow", None))
        self.boton_v_cierre.setText(QCoreApplication.translate("MainPrincipal", u"CIERRE", None))
        self.boton_v_configuracion.setText(QCoreApplication.translate("MainPrincipal", u"CONFIGURACI\u00d3N", None))
        self.boton_v_cerrar_sesion.setText(QCoreApplication.translate("MainPrincipal", u"CERRAR SESI\u00d3N", None))
        self.logo.setText("")
        self.boton_v_facturar.setText(QCoreApplication.translate("MainPrincipal", u"FACTURAR", None))
        self.boton_v_clientes.setText(QCoreApplication.translate("MainPrincipal", u"CLIENTES", None))
        self.boton_v_productos.setText(QCoreApplication.translate("MainPrincipal", u"PRODUCTOS", None))
        self.boton_v_registrar.setText(QCoreApplication.translate("MainPrincipal", u"REGISTRAR", None))
        self.boton_v_registrar_clientes.setText(QCoreApplication.translate("MainPrincipal", u"REGISTRAR\n"
"CLIENTES", None))
        self.boton_v_registar_productos.setText(QCoreApplication.translate("MainPrincipal", u"REGISTRAR\n"
"PRODUCTOS", None))
        self.line_telefono_rcliente.setPlaceholderText(QCoreApplication.translate("MainPrincipal", u"TELEFONO", None))
        self.line_nombre_rcliente.setPlaceholderText(QCoreApplication.translate("MainPrincipal", u"NOMBRE", None))
        self.combo_nacionalidad_rcliente.setItemText(0, QCoreApplication.translate("MainPrincipal", u"V", None))
        self.combo_nacionalidad_rcliente.setItemText(1, QCoreApplication.translate("MainPrincipal", u"E", None))
        self.combo_nacionalidad_rcliente.setItemText(2, QCoreApplication.translate("MainPrincipal", u"J", None))

        self.line_cedula_rcliente.setText("")
        self.line_cedula_rcliente.setPlaceholderText(QCoreApplication.translate("MainPrincipal", u"CEDULA", None))
        self.boton_buscar_rcliente.setText(QCoreApplication.translate("MainPrincipal", u"BUSCAR CLIENTE", None))
        self.text_descripcion_rcliente.setPlaceholderText(QCoreApplication.translate("MainPrincipal", u"DIRECCI\u00d3N (OPCIONAL)", None))
        self.check_editar_rcliente.setText(QCoreApplication.translate("MainPrincipal", u"EDITAR", None))
        self.line_apellido_rcliente.setPlaceholderText(QCoreApplication.translate("MainPrincipal", u"APELLIDO", None))
        self.boton_registrar_rcliente.setText(QCoreApplication.translate("MainPrincipal", u"REGISTRAR", None))
        self.boton_buscar_producto_facturar.setText(QCoreApplication.translate("MainPrincipal", u"BUSCAR PRODUCTO", None))
        self.line_cedula_facturar.setPlaceholderText(QCoreApplication.translate("MainPrincipal", u"CEDULA", None))
        self.boton_buscar_cliente_facturar.setText(QCoreApplication.translate("MainPrincipal", u"BUSCAR", None))
        self.label_bs_facturar.setText(QCoreApplication.translate("MainPrincipal", u"Valor BS:", None))
        self.label_dolar_facturar.setText(QCoreApplication.translate("MainPrincipal", u"Valor $:", None))
        self.label_cop_facturar.setText(QCoreApplication.translate("MainPrincipal", u"Valor COP:", None))
        self.boton_facturar.setText(QCoreApplication.translate("MainPrincipal", u"FACTURAR", None))
        self.line_nombre_facturar.setText("")
        self.line_nombre_facturar.setPlaceholderText(QCoreApplication.translate("MainPrincipal", u"NOMBRE", None))
        self.combo_nacionalidad_facturar.setItemText(0, QCoreApplication.translate("MainPrincipal", u"V", None))
        self.combo_nacionalidad_facturar.setItemText(1, QCoreApplication.translate("MainPrincipal", u"E", None))

        self.line_apellido_facturar.setText("")
        self.line_apellido_facturar.setPlaceholderText(QCoreApplication.translate("MainPrincipal", u"APELLIDO", None))
        self.label_total.setText(QCoreApplication.translate("MainPrincipal", u"TOTAL EN DOLARES:", None))
        self.line_bclientes.setPlaceholderText(QCoreApplication.translate("MainPrincipal", u"CEDULA", None))
        self.boton_buscar_bclientes.setText(QCoreApplication.translate("MainPrincipal", u"BUSCAR", None))
        self.combo_buscar_bclientes.setItemText(0, QCoreApplication.translate("MainPrincipal", u"CEDULA", None))
        self.combo_buscar_bclientes.setItemText(1, QCoreApplication.translate("MainPrincipal", u"NOMBRE", None))
        self.combo_buscar_bclientes.setItemText(2, QCoreApplication.translate("MainPrincipal", u"APELLIDO", None))

        self.line_bproducto.setPlaceholderText(QCoreApplication.translate("MainPrincipal", u"NOMBRE", None))
        self.boton_buscar_bproducto.setText(QCoreApplication.translate("MainPrincipal", u"BUSCAR", None))
        self.combo_buscar_bproducto.setItemText(0, QCoreApplication.translate("MainPrincipal", u"NOMBRE", None))
        self.combo_buscar_bproducto.setItemText(1, QCoreApplication.translate("MainPrincipal", u"PRECIO", None))
        self.combo_buscar_bproducto.setItemText(2, QCoreApplication.translate("MainPrincipal", u"ID", None))

        self.cop_cierre.setText(QCoreApplication.translate("MainPrincipal", u"TextLabel", None))
        self.total_dolares_cierre.setText(QCoreApplication.translate("MainPrincipal", u"TOTAL BS:", None))
        self.label_tasa_cop_cierre.setText(QCoreApplication.translate("MainPrincipal", u"TASA COP:", None))
        self.tasa_bcv_cierre.setText(QCoreApplication.translate("MainPrincipal", u"TASA BCV:", None))
        self.bs_cierre.setText(QCoreApplication.translate("MainPrincipal", u"TextLabel", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainPrincipal", u"IMPRIMIR", None))
        self.total_cop_cierre.setText(QCoreApplication.translate("MainPrincipal", u"TOTAL COP:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainPrincipal", u"CAMBIOS", None))
        self.dolares_cierre.setText(QCoreApplication.translate("MainPrincipal", u"TextLabel", None))
        self.label_total_dolares_cierre.setText(QCoreApplication.translate("MainPrincipal", u"TOTAL DOLARES:", None))
        self.pushButton.setText(QCoreApplication.translate("MainPrincipal", u"GENERAR", None))
        self.label_2.setText(QCoreApplication.translate("MainPrincipal", u"EN DESARROLLO.....", None))
        self.label_3.setText(QCoreApplication.translate("MainPrincipal", u"EN DESARROLLO.....", None))
        self.line_nombre_rproducto.setPlaceholderText(QCoreApplication.translate("MainPrincipal", u"NOMBRE PRODUCTO", None))
        self.text_descripcion_rproducto.setPlaceholderText(QCoreApplication.translate("MainPrincipal", u"DESCRIPCI\u00d3N DEL PRODUCTO (OPCIONAL)", None))
        self.label_precio.setText(QCoreApplication.translate("MainPrincipal", u"PRECI\u00d3 EN DOLARES:", None))
        self.boton_registrar_rproducto.setText(QCoreApplication.translate("MainPrincipal", u"REGISTRAR", None))
    # retranslateUi

