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
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u"images/zone.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"	font-size: 12px;\n"
"	font-family: Rockwell;\n"
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
"	border-left: 1px solid white;\n"
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
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.contenedor_principal = QWidget(self.centralwidget)
        self.contenedor_principal.setObjectName(u"contenedor_principal")
        self.contenedor_principal.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.contenedor_principal)
        self.gridLayout.setObjectName(u"gridLayout")
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
"QLineEdit:disabled,QTextEdit:disabled{\n"
"	color: rgb(0, 0, 255);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image: url(\"images/lock.png\");\n"
"	width: 25px;\n"
"}\n"
"\n"
"QCheckBox::indic"
                        "ator:unchecked{\n"
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
"QDoubleSpinB"
                        "ox, QSpinBox,QDateEdit {\n"
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
"QScrollBar::handle"
                        ":vertical {\n"
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
        self.vista_divisas = QWidget()
        self.vista_divisas.setObjectName(u"vista_divisas")
        self.vista_divisas.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.vista_divisas)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(14)
        self.gridLayout_7.setContentsMargins(-1, 16, -1, 16)
        self.combo_divisa_adivisa = QComboBox(self.vista_divisas)
        self.combo_divisa_adivisa.addItem("")
        self.combo_divisa_adivisa.addItem("")
        self.combo_divisa_adivisa.setObjectName(u"combo_divisa_adivisa")
        self.combo_divisa_adivisa.setCursor(QCursor(Qt.PointingHandCursor))
        self.combo_divisa_adivisa.setStyleSheet(u"min-width: 8em;")

        self.gridLayout_7.addWidget(self.combo_divisa_adivisa, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(self.vista_divisas)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 14px;")

        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.boton_actualizar_adivisa = QPushButton(self.vista_divisas)
        self.boton_actualizar_adivisa.setObjectName(u"boton_actualizar_adivisa")
        self.boton_actualizar_adivisa.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_7.addWidget(self.boton_actualizar_adivisa, 3, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.double_valor_adivisa = QDoubleSpinBox(self.vista_divisas)
        self.double_valor_adivisa.setObjectName(u"double_valor_adivisa")
        self.double_valor_adivisa.setCursor(QCursor(Qt.PointingHandCursor))
        self.double_valor_adivisa.setMaximum(9999999999.000000000000000)

        self.gridLayout_7.addWidget(self.double_valor_adivisa, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 4, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_7)

        self.stacked_widget.addWidget(self.vista_divisas)
        self.vista_registrar_clientes = QWidget()
        self.vista_registrar_clientes.setObjectName(u"vista_registrar_clientes")
        self.verticalLayout_3 = QVBoxLayout(self.vista_registrar_clientes)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.layout_registrar_clientes = QGridLayout()
        self.layout_registrar_clientes.setObjectName(u"layout_registrar_clientes")
        self.line_nombre_rcliente = QLineEdit(self.vista_registrar_clientes)
        self.line_nombre_rcliente.setObjectName(u"line_nombre_rcliente")
        self.line_nombre_rcliente.setEnabled(True)
        self.line_nombre_rcliente.setCursorPosition(0)
        self.line_nombre_rcliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_registrar_clientes.addWidget(self.line_nombre_rcliente, 5, 0, 1, 1)

        self.boton_registrar_rcliente = QPushButton(self.vista_registrar_clientes)
        self.boton_registrar_rcliente.setObjectName(u"boton_registrar_rcliente")
        self.boton_registrar_rcliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_registrar_clientes.addWidget(self.boton_registrar_rcliente, 9, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.boton_buscar_rcliente = QPushButton(self.vista_registrar_clientes)
        self.boton_buscar_rcliente.setObjectName(u"boton_buscar_rcliente")
        self.boton_buscar_rcliente.setEnabled(True)
        self.boton_buscar_rcliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_registrar_clientes.addWidget(self.boton_buscar_rcliente, 1, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.line_telefono_rcliente = QLineEdit(self.vista_registrar_clientes)
        self.line_telefono_rcliente.setObjectName(u"line_telefono_rcliente")
        self.line_telefono_rcliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_registrar_clientes.addWidget(self.line_telefono_rcliente, 8, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.text_descripcion_rcliente = QTextEdit(self.vista_registrar_clientes)
        self.text_descripcion_rcliente.setObjectName(u"text_descripcion_rcliente")
        self.text_descripcion_rcliente.setTabChangesFocus(True)

        self.layout_registrar_clientes.addWidget(self.text_descripcion_rcliente, 7, 0, 1, 2)

        self.line_apellido_rcliente = QLineEdit(self.vista_registrar_clientes)
        self.line_apellido_rcliente.setObjectName(u"line_apellido_rcliente")
        self.line_apellido_rcliente.setCursorPosition(0)
        self.line_apellido_rcliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_registrar_clientes.addWidget(self.line_apellido_rcliente, 5, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.combo_nacionalidad_rcliente = QComboBox(self.vista_registrar_clientes)
        self.combo_nacionalidad_rcliente.addItem("")
        self.combo_nacionalidad_rcliente.addItem("")
        self.combo_nacionalidad_rcliente.setObjectName(u"combo_nacionalidad_rcliente")
        self.combo_nacionalidad_rcliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.combo_nacionalidad_rcliente, 0, Qt.AlignmentFlag.AlignLeft)

        self.line_cedula_rcliente = QLineEdit(self.vista_registrar_clientes)
        self.line_cedula_rcliente.setObjectName(u"line_cedula_rcliente")
        self.line_cedula_rcliente.setCursorPosition(0)
        self.line_cedula_rcliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.line_cedula_rcliente)


        self.layout_registrar_clientes.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)

        self.check_editar_rcliente = QCheckBox(self.vista_registrar_clientes)
        self.check_editar_rcliente.setObjectName(u"check_editar_rcliente")
        self.check_editar_rcliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_registrar_clientes.addWidget(self.check_editar_rcliente, 2, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_3.addLayout(self.layout_registrar_clientes)

        self.stacked_widget.addWidget(self.vista_registrar_clientes)
        self.vista_actualizar_productos = QWidget()
        self.vista_actualizar_productos.setObjectName(u"vista_actualizar_productos")
        self.verticalLayout_15 = QVBoxLayout(self.vista_actualizar_productos)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(16)
        self.gridLayout_3.setContentsMargins(16, 16, 16, 16)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.boton_actualizar_aproducto = QPushButton(self.vista_actualizar_productos)
        self.boton_actualizar_aproducto.setObjectName(u"boton_actualizar_aproducto")
        self.boton_actualizar_aproducto.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.boton_actualizar_aproducto, 5, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel(self.vista_actualizar_productos)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 14px;")

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.line_nombre_aproducto = QLineEdit(self.vista_actualizar_productos)
        self.line_nombre_aproducto.setObjectName(u"line_nombre_aproducto")
        self.line_nombre_aproducto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.line_nombre_aproducto, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.text_descripcion_aproducto = QTextEdit(self.vista_actualizar_productos)
        self.text_descripcion_aproducto.setObjectName(u"text_descripcion_aproducto")
        self.text_descripcion_aproducto.setTabChangesFocus(True)

        self.gridLayout_3.addWidget(self.text_descripcion_aproducto, 3, 0, 1, 1)

        self.boton_volver_aproducto = QPushButton(self.vista_actualizar_productos)
        self.boton_volver_aproducto.setObjectName(u"boton_volver_aproducto")
        self.boton_volver_aproducto.setCursor(QCursor(Qt.PointingHandCursor))
        self.boton_volver_aproducto.setStyleSheet(u"margin-left: 1em;")

        self.gridLayout_3.addWidget(self.boton_volver_aproducto, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.double_precio_aproducto = QDoubleSpinBox(self.vista_actualizar_productos)
        self.double_precio_aproducto.setObjectName(u"double_precio_aproducto")
        self.double_precio_aproducto.setCursor(QCursor(Qt.PointingHandCursor))
        self.double_precio_aproducto.setMaximum(9999999999.000000000000000)

        self.gridLayout_3.addWidget(self.double_precio_aproducto, 4, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.boton_borrar_aproducto = QPushButton(self.vista_actualizar_productos)
        self.boton_borrar_aproducto.setObjectName(u"boton_borrar_aproducto")
        self.boton_borrar_aproducto.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.boton_borrar_aproducto, 6, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_15.addLayout(self.gridLayout_3)

        self.stacked_widget.addWidget(self.vista_actualizar_productos)
        self.vista_facturar = QWidget()
        self.vista_facturar.setObjectName(u"vista_facturar")
        self.verticalLayout_13 = QVBoxLayout(self.vista_facturar)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_cop_facturar = QLabel(self.vista_facturar)
        self.label_cop_facturar.setObjectName(u"label_cop_facturar")

        self.gridLayout_5.addWidget(self.label_cop_facturar, 1, 4, 1, 1)

        self.label_dolar = QLabel(self.vista_facturar)
        self.label_dolar.setObjectName(u"label_dolar")
        self.label_dolar.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.label_dolar, 1, 1, 1, 1)

        self.label_dolar_facturar = QLabel(self.vista_facturar)
        self.label_dolar_facturar.setObjectName(u"label_dolar_facturar")

        self.gridLayout_5.addWidget(self.label_dolar_facturar, 1, 0, 1, 1)

        self.label_bs_facturar = QLabel(self.vista_facturar)
        self.label_bs_facturar.setObjectName(u"label_bs_facturar")

        self.gridLayout_5.addWidget(self.label_bs_facturar, 1, 2, 1, 1)

        self.double_dolares_facturar = QDoubleSpinBox(self.vista_facturar)
        self.double_dolares_facturar.setObjectName(u"double_dolares_facturar")
        self.double_dolares_facturar.setCursor(QCursor(Qt.PointingHandCursor))
        self.double_dolares_facturar.setMaximum(999999999.990000009536743)

        self.gridLayout_5.addWidget(self.double_dolares_facturar, 0, 0, 1, 2)

        self.label_bs = QLabel(self.vista_facturar)
        self.label_bs.setObjectName(u"label_bs")
        self.label_bs.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.label_bs, 1, 3, 1, 1)

        self.label_cop = QLabel(self.vista_facturar)
        self.label_cop.setObjectName(u"label_cop")
        self.label_cop.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.label_cop, 1, 5, 1, 1)

        self.double_bs_facturar = QDoubleSpinBox(self.vista_facturar)
        self.double_bs_facturar.setObjectName(u"double_bs_facturar")
        self.double_bs_facturar.setCursor(QCursor(Qt.PointingHandCursor))
        self.double_bs_facturar.setMaximum(999999999.990000009536743)

        self.gridLayout_5.addWidget(self.double_bs_facturar, 0, 2, 1, 2)

        self.spin_cop_facturar = QSpinBox(self.vista_facturar)
        self.spin_cop_facturar.setObjectName(u"spin_cop_facturar")
        self.spin_cop_facturar.setCursor(QCursor(Qt.PointingHandCursor))
        self.spin_cop_facturar.setMinimum(0)
        self.spin_cop_facturar.setMaximum(999999999)
        self.spin_cop_facturar.setSingleStep(1000)
        self.spin_cop_facturar.setDisplayIntegerBase(10)

        self.gridLayout_5.addWidget(self.spin_cop_facturar, 0, 4, 1, 2)


        self.gridLayout_4.addLayout(self.gridLayout_5, 7, 0, 1, 3)

        self.line_apellido_facturar = QLineEdit(self.vista_facturar)
        self.line_apellido_facturar.setObjectName(u"line_apellido_facturar")
        self.line_apellido_facturar.setEnabled(False)
        self.line_apellido_facturar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.line_apellido_facturar, 1, 2, 1, 1)

        self.table_productos_facturar = QTableWidget(self.vista_facturar)
        if (self.table_productos_facturar.columnCount() < 5):
            self.table_productos_facturar.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_productos_facturar.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_productos_facturar.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_productos_facturar.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_productos_facturar.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_productos_facturar.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table_productos_facturar.setObjectName(u"table_productos_facturar")
        self.table_productos_facturar.setEnabled(True)
        self.table_productos_facturar.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_productos_facturar.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_productos_facturar.horizontalHeader().setCascadingSectionResizes(False)
        self.table_productos_facturar.horizontalHeader().setDefaultSectionSize(110)
        self.table_productos_facturar.horizontalHeader().setStretchLastSection(True)
        self.table_productos_facturar.verticalHeader().setVisible(False)

        self.gridLayout_4.addWidget(self.table_productos_facturar, 3, 0, 1, 3)

        self.boton_buscar_producto_facturar = QPushButton(self.vista_facturar)
        self.boton_buscar_producto_facturar.setObjectName(u"boton_buscar_producto_facturar")
        self.boton_buscar_producto_facturar.setMinimumSize(QSize(140, 0))
        self.boton_buscar_producto_facturar.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.boton_buscar_producto_facturar, 2, 1, 1, 1)

        self.boton_facturar = QPushButton(self.vista_facturar)
        self.boton_facturar.setObjectName(u"boton_facturar")
        self.boton_facturar.setMinimumSize(QSize(140, 0))
        self.boton_facturar.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.boton_facturar, 8, 1, 1, 1)

        self.line_nombre_facturar = QLineEdit(self.vista_facturar)
        self.line_nombre_facturar.setObjectName(u"line_nombre_facturar")
        self.line_nombre_facturar.setEnabled(False)
        self.line_nombre_facturar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.line_nombre_facturar, 1, 0, 1, 1)

        self.label_total = QLabel(self.vista_facturar)
        self.label_total.setObjectName(u"label_total")

        self.gridLayout_4.addWidget(self.label_total, 4, 0, 1, 2)

        self.line_cedula_facturar = QLineEdit(self.vista_facturar)
        self.line_cedula_facturar.setObjectName(u"line_cedula_facturar")

        self.gridLayout_4.addWidget(self.line_cedula_facturar, 0, 1, 1, 1)

        self.combo_nacionalidad_facturar = QComboBox(self.vista_facturar)
        self.combo_nacionalidad_facturar.addItem("")
        self.combo_nacionalidad_facturar.addItem("")
        self.combo_nacionalidad_facturar.setObjectName(u"combo_nacionalidad_facturar")
        self.combo_nacionalidad_facturar.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.combo_nacionalidad_facturar, 0, 0, 1, 1)

        self.boton_buscar_cliente_facturar = QPushButton(self.vista_facturar)
        self.boton_buscar_cliente_facturar.setObjectName(u"boton_buscar_cliente_facturar")
        self.boton_buscar_cliente_facturar.setMinimumSize(QSize(140, 0))
        self.boton_buscar_cliente_facturar.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.boton_buscar_cliente_facturar, 0, 2, 1, 1, Qt.AlignmentFlag.AlignBottom)

        self.label_total_iva = QLabel(self.vista_facturar)
        self.label_total_iva.setObjectName(u"label_total_iva")

        self.gridLayout_4.addWidget(self.label_total_iva, 6, 0, 1, 2)

        self.label_iva = QLabel(self.vista_facturar)
        self.label_iva.setObjectName(u"label_iva")

        self.gridLayout_4.addWidget(self.label_iva, 5, 0, 1, 2)


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
        self.combo_buscar_bproducto.setObjectName(u"combo_buscar_bproducto")
        self.combo_buscar_bproducto.setMinimumSize(QSize(56, 0))
        self.combo_buscar_bproducto.setCursor(QCursor(Qt.PointingHandCursor))
        self.combo_buscar_bproducto.setStyleSheet(u"min-width: 4em;")

        self.gridLayout_2.addWidget(self.combo_buscar_bproducto, 0, 0, 1, 1)

        self.table_productos = QTableWidget(self.vista_productos)
        if (self.table_productos.columnCount() < 4):
            self.table_productos.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_productos.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_productos.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_productos.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_productos.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        self.table_productos.setObjectName(u"table_productos")
        self.table_productos.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_productos.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_productos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_productos.setShowGrid(False)
        self.table_productos.setRowCount(0)
        self.table_productos.setColumnCount(4)
        self.table_productos.horizontalHeader().setCascadingSectionResizes(False)
        self.table_productos.horizontalHeader().setDefaultSectionSize(130)
        self.table_productos.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_productos.horizontalHeader().setStretchLastSection(True)
        self.table_productos.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.table_productos, 1, 0, 1, 3)


        self.verticalLayout_9.addLayout(self.gridLayout_2)

        self.stacked_widget.addWidget(self.vista_productos)
        self.vista_cierre = QWidget()
        self.vista_cierre.setObjectName(u"vista_cierre")
        self.verticalLayout_7 = QVBoxLayout(self.vista_cierre)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.botont_rehacer_cierre = QPushButton(self.vista_cierre)
        self.botont_rehacer_cierre.setObjectName(u"botont_rehacer_cierre")
        self.botont_rehacer_cierre.setEnabled(False)
        self.botont_rehacer_cierre.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_6.addWidget(self.botont_rehacer_cierre, 9, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.date_cierre = QDateEdit(self.vista_cierre)
        self.date_cierre.setObjectName(u"date_cierre")
        self.date_cierre.setCursor(QCursor(Qt.PointingHandCursor))
        self.date_cierre.setCalendarPopup(True)
        self.date_cierre.setTimeSpec(Qt.TimeSpec.UTC)
        self.date_cierre.setDate(QDate(2024, 1, 1))

        self.gridLayout_6.addWidget(self.date_cierre, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.label_bs_cierre = QLabel(self.vista_cierre)
        self.label_bs_cierre.setObjectName(u"label_bs_cierre")

        self.gridLayout_6.addWidget(self.label_bs_cierre, 3, 1, 1, 1)

        self.boton_realizar_cierre = QPushButton(self.vista_cierre)
        self.boton_realizar_cierre.setObjectName(u"boton_realizar_cierre")
        self.boton_realizar_cierre.setEnabled(False)
        self.boton_realizar_cierre.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_6.addWidget(self.boton_realizar_cierre, 8, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.label_3 = QLabel(self.vista_cierre)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_5 = QLabel(self.vista_cierre)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 5, 0, 1, 1)

        self.boton_buscar_cierre = QPushButton(self.vista_cierre)
        self.boton_buscar_cierre.setObjectName(u"boton_buscar_cierre")
        self.boton_buscar_cierre.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_6.addWidget(self.boton_buscar_cierre, 1, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.label_cop_cierre = QLabel(self.vista_cierre)
        self.label_cop_cierre.setObjectName(u"label_cop_cierre")

        self.gridLayout_6.addWidget(self.label_cop_cierre, 5, 1, 1, 1)

        self.table_facturas_cierre = QTableWidget(self.vista_cierre)
        if (self.table_facturas_cierre.columnCount() < 5):
            self.table_facturas_cierre.setColumnCount(5)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_facturas_cierre.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_facturas_cierre.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_facturas_cierre.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_facturas_cierre.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_facturas_cierre.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        self.table_facturas_cierre.setObjectName(u"table_facturas_cierre")
        self.table_facturas_cierre.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_facturas_cierre.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_facturas_cierre.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_facturas_cierre.setShowGrid(False)
        self.table_facturas_cierre.setRowCount(0)
        self.table_facturas_cierre.setColumnCount(5)
        self.table_facturas_cierre.horizontalHeader().setCascadingSectionResizes(False)
        self.table_facturas_cierre.horizontalHeader().setDefaultSectionSize(109)
        self.table_facturas_cierre.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_facturas_cierre.horizontalHeader().setStretchLastSection(True)
        self.table_facturas_cierre.verticalHeader().setVisible(False)

        self.gridLayout_6.addWidget(self.table_facturas_cierre, 2, 0, 1, 2)

        self.label_4 = QLabel(self.vista_cierre)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 6, 0, 1, 1)

        self.label_dolar_cierre = QLabel(self.vista_cierre)
        self.label_dolar_cierre.setObjectName(u"label_dolar_cierre")

        self.gridLayout_6.addWidget(self.label_dolar_cierre, 6, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_6)

        self.stacked_widget.addWidget(self.vista_cierre)
        self.vista_configuracion = QWidget()
        self.vista_configuracion.setObjectName(u"vista_configuracion")
        self.vista_configuracion.setStyleSheet(u"QPushButton{\n"
"	min-width: 14em;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.vista_configuracion)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.boton_configurar_bd = QPushButton(self.vista_configuracion)
        self.boton_configurar_bd.setObjectName(u"boton_configurar_bd")
        self.boton_configurar_bd.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.boton_configurar_bd, 0, Qt.AlignmentFlag.AlignHCenter)

        self.boton_registrar_usuarios = QPushButton(self.vista_configuracion)
        self.boton_registrar_usuarios.setObjectName(u"boton_registrar_usuarios")
        self.boton_registrar_usuarios.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.boton_registrar_usuarios, 0, Qt.AlignmentFlag.AlignHCenter)

        self.boton_v_cambiar_usuarios = QPushButton(self.vista_configuracion)
        self.boton_v_cambiar_usuarios.setObjectName(u"boton_v_cambiar_usuarios")
        self.boton_v_cambiar_usuarios.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.boton_v_cambiar_usuarios, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)


        self.verticalLayout_11.addLayout(self.verticalLayout_5)

        self.stacked_widget.addWidget(self.vista_configuracion)
        self.vista_editar_clientes = QWidget()
        self.vista_editar_clientes.setObjectName(u"vista_editar_clientes")
        self.verticalLayout_8 = QVBoxLayout(self.vista_editar_clientes)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.layout_registrar_clientes_2 = QGridLayout()
        self.layout_registrar_clientes_2.setObjectName(u"layout_registrar_clientes_2")
        self.boton_actualizar_ecliente = QPushButton(self.vista_editar_clientes)
        self.boton_actualizar_ecliente.setObjectName(u"boton_actualizar_ecliente")
        self.boton_actualizar_ecliente.setEnabled(False)
        self.boton_actualizar_ecliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_registrar_clientes_2.addWidget(self.boton_actualizar_ecliente, 8, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.line_nombre_ecliente = QLineEdit(self.vista_editar_clientes)
        self.line_nombre_ecliente.setObjectName(u"line_nombre_ecliente")
        self.line_nombre_ecliente.setEnabled(False)
        self.line_nombre_ecliente.setCursorPosition(0)
        self.line_nombre_ecliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_registrar_clientes_2.addWidget(self.line_nombre_ecliente, 4, 0, 1, 1)

        self.line_telefono_ecliente = QLineEdit(self.vista_editar_clientes)
        self.line_telefono_ecliente.setObjectName(u"line_telefono_ecliente")
        self.line_telefono_ecliente.setEnabled(False)
        self.line_telefono_ecliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_registrar_clientes_2.addWidget(self.line_telefono_ecliente, 7, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.line_apellido_ecliente = QLineEdit(self.vista_editar_clientes)
        self.line_apellido_ecliente.setObjectName(u"line_apellido_ecliente")
        self.line_apellido_ecliente.setEnabled(False)
        self.line_apellido_ecliente.setCursorPosition(0)
        self.line_apellido_ecliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_registrar_clientes_2.addWidget(self.line_apellido_ecliente, 4, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.combo_nacionalidad_ecliente = QComboBox(self.vista_editar_clientes)
        self.combo_nacionalidad_ecliente.addItem("")
        self.combo_nacionalidad_ecliente.addItem("")
        self.combo_nacionalidad_ecliente.setObjectName(u"combo_nacionalidad_ecliente")
        self.combo_nacionalidad_ecliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.combo_nacionalidad_ecliente, 0, Qt.AlignmentFlag.AlignLeft)

        self.line_cedula_ecliente = QLineEdit(self.vista_editar_clientes)
        self.line_cedula_ecliente.setObjectName(u"line_cedula_ecliente")
        self.line_cedula_ecliente.setCursorPosition(0)
        self.line_cedula_ecliente.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.line_cedula_ecliente)

        self.boton_buscar_ecliente = QPushButton(self.vista_editar_clientes)
        self.boton_buscar_ecliente.setObjectName(u"boton_buscar_ecliente")
        self.boton_buscar_ecliente.setEnabled(True)
        self.boton_buscar_ecliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.boton_buscar_ecliente, 0, Qt.AlignmentFlag.AlignVCenter)


        self.layout_registrar_clientes_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 2)

        self.text_descripcion_ecliente = QTextEdit(self.vista_editar_clientes)
        self.text_descripcion_ecliente.setObjectName(u"text_descripcion_ecliente")
        self.text_descripcion_ecliente.setEnabled(False)
        self.text_descripcion_ecliente.setTabChangesFocus(True)

        self.layout_registrar_clientes_2.addWidget(self.text_descripcion_ecliente, 6, 0, 1, 2)

        self.boton_borrar_ecliente = QPushButton(self.vista_editar_clientes)
        self.boton_borrar_ecliente.setObjectName(u"boton_borrar_ecliente")
        self.boton_borrar_ecliente.setEnabled(False)
        self.boton_borrar_ecliente.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_registrar_clientes_2.addWidget(self.boton_borrar_ecliente, 9, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_8.addLayout(self.layout_registrar_clientes_2)

        self.stacked_widget.addWidget(self.vista_editar_clientes)
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
        self.line_nombre_rproducto.setMinimumSize(QSize(162, 0))
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
        self.double_precio_rproducto.setCursor(QCursor(Qt.PointingHandCursor))
        self.double_precio_rproducto.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.double_precio_rproducto.setMaximum(9999999999.000000000000000)

        self.layout_registrar_productos.addWidget(self.double_precio_rproducto, 0, Qt.AlignmentFlag.AlignHCenter)

        self.boton_registrar_rproducto = QPushButton(self.vista_registrar_productos)
        self.boton_registrar_rproducto.setObjectName(u"boton_registrar_rproducto")
        self.boton_registrar_rproducto.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_registrar_productos.addWidget(self.boton_registrar_rproducto, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_registrar_productos.addItem(self.verticalSpacer_3)


        self.verticalLayout_6.addLayout(self.layout_registrar_productos)

        self.stacked_widget.addWidget(self.vista_registrar_productos)

        self.gridLayout.addWidget(self.stacked_widget, 1, 1, 1, 3)

        self.contenedor_logo = QWidget(self.contenedor_principal)
        self.contenedor_logo.setObjectName(u"contenedor_logo")
        self.contenedor_logo.setMinimumSize(QSize(0, 120))
        self.contenedor_logo.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.contenedor_logo)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.contenedor_logo)
        self.logo.setObjectName(u"logo")
        self.logo.setEnabled(True)
        self.logo.setMinimumSize(QSize(0, 120))
        self.logo.setMaximumSize(QSize(120, 120))
        self.logo.setPixmap(QPixmap(u"images/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.logo, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.contenedor_logo, 0, 0, 1, 1)

        self.widget_lateral = QWidget(self.contenedor_principal)
        self.widget_lateral.setObjectName(u"widget_lateral")
        self.widget_lateral.setStyleSheet(u"min-width:10em;")
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

        self.boton_v_divisas = QPushButton(self.widget_lateral)
        self.boton_v_divisas.setObjectName(u"boton_v_divisas")
        self.boton_v_divisas.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.boton_v_divisas)

        self.boton_v_registar_productos = QPushButton(self.widget_lateral)
        self.boton_v_registar_productos.setObjectName(u"boton_v_registar_productos")
        self.boton_v_registar_productos.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.boton_v_registar_productos)

        self.boton_v_registrar_clientes = QPushButton(self.widget_lateral)
        self.boton_v_registrar_clientes.setObjectName(u"boton_v_registrar_clientes")
        self.boton_v_registrar_clientes.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.boton_v_registrar_clientes)

        self.boton_v_editar_clientes = QPushButton(self.widget_lateral)
        self.boton_v_editar_clientes.setObjectName(u"boton_v_editar_clientes")
        self.boton_v_editar_clientes.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.boton_v_editar_clientes)

        self.boton_v_editar_facturas = QPushButton(self.widget_lateral)
        self.boton_v_editar_facturas.setObjectName(u"boton_v_editar_facturas")
        self.boton_v_editar_facturas.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.boton_v_editar_facturas)


        self.gridLayout.addWidget(self.widget_lateral, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.widget_superior = QWidget(self.contenedor_principal)
        self.widget_superior.setObjectName(u"widget_superior")
        self.horizontalLayout = QHBoxLayout(self.widget_superior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.boton_v_cierre = QPushButton(self.widget_superior)
        self.boton_v_cierre.setObjectName(u"boton_v_cierre")
        self.boton_v_cierre.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.boton_v_cierre)

        self.boton_v_data = QPushButton(self.widget_superior)
        self.boton_v_data.setObjectName(u"boton_v_data")
        self.boton_v_data.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.boton_v_data)

        self.boton_v_configuracion = QPushButton(self.widget_superior)
        self.boton_v_configuracion.setObjectName(u"boton_v_configuracion")
        self.boton_v_configuracion.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.boton_v_configuracion)

        self.boton_v_cerrar_sesion = QPushButton(self.widget_superior)
        self.boton_v_cerrar_sesion.setObjectName(u"boton_v_cerrar_sesion")
        self.boton_v_cerrar_sesion.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.boton_v_cerrar_sesion)


        self.gridLayout.addWidget(self.widget_superior, 0, 3, 1, 1)

        self.gridLayout.setColumnStretch(2, 1)

        self.horizontalLayout_2.addWidget(self.contenedor_principal)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.boton_v_facturar, self.boton_v_productos)
        QWidget.setTabOrder(self.boton_v_productos, self.line_nombre_rproducto)
        QWidget.setTabOrder(self.line_nombre_rproducto, self.text_descripcion_rproducto)
        QWidget.setTabOrder(self.text_descripcion_rproducto, self.double_precio_rproducto)
        QWidget.setTabOrder(self.double_precio_rproducto, self.boton_registrar_rproducto)
        QWidget.setTabOrder(self.boton_registrar_rproducto, self.boton_v_configuracion)
        QWidget.setTabOrder(self.boton_v_configuracion, self.line_telefono_rcliente)
        QWidget.setTabOrder(self.line_telefono_rcliente, self.boton_registrar_rcliente)
        QWidget.setTabOrder(self.boton_registrar_rcliente, self.boton_buscar_rcliente)
        QWidget.setTabOrder(self.boton_buscar_rcliente, self.text_descripcion_rcliente)
        QWidget.setTabOrder(self.text_descripcion_rcliente, self.line_apellido_rcliente)
        QWidget.setTabOrder(self.line_apellido_rcliente, self.line_nombre_rcliente)

        self.retranslateUi(MainWindow)

        self.stacked_widget.setCurrentIndex(8)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FRIKIZONE", None))
        self.combo_divisa_adivisa.setItemText(0, QCoreApplication.translate("MainWindow", u"BOLIVAR", None))
        self.combo_divisa_adivisa.setItemText(1, QCoreApplication.translate("MainWindow", u"COP", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR DIVISAS", None))
        self.boton_actualizar_adivisa.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.line_nombre_rcliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.boton_registrar_rcliente.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.boton_buscar_rcliente.setText(QCoreApplication.translate("MainWindow", u"BUSCAR CLIENTE CNE", None))
        self.line_telefono_rcliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONO", None))
        self.text_descripcion_rcliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DIRECCI\u00d3N (OPCIONAL)", None))
        self.line_apellido_rcliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"APELLIDO", None))
        self.combo_nacionalidad_rcliente.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.combo_nacionalidad_rcliente.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))

        self.line_cedula_rcliente.setText("")
        self.line_cedula_rcliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEDULA", None))
        self.check_editar_rcliente.setText(QCoreApplication.translate("MainWindow", u"EDITAR", None))
        self.boton_actualizar_aproducto.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR PRODUCTO", None))
        self.line_nombre_aproducto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE PRODUCTO", None))
        self.text_descripcion_aproducto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DESCRIPCI\u00d3N DEL PRODUCTO", None))
        self.boton_volver_aproducto.setText(QCoreApplication.translate("MainWindow", u"VOLVER", None))
        self.boton_borrar_aproducto.setText(QCoreApplication.translate("MainWindow", u"BORRAR PRODUCTO", None))
        self.label_cop_facturar.setText(QCoreApplication.translate("MainWindow", u"Valor COP:", None))
        self.label_dolar.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_dolar_facturar.setText(QCoreApplication.translate("MainWindow", u"Valor $:", None))
        self.label_bs_facturar.setText(QCoreApplication.translate("MainWindow", u"Valor BS:", None))
        self.label_bs.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_cop.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.line_apellido_facturar.setText("")
        self.line_apellido_facturar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"APELLIDO", None))
        ___qtablewidgetitem = self.table_productos_facturar.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table_productos_facturar.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PRODUCTO", None));
        ___qtablewidgetitem2 = self.table_productos_facturar.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None));
        ___qtablewidgetitem3 = self.table_productos_facturar.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"CANTIDAD", None));
        ___qtablewidgetitem4 = self.table_productos_facturar.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"SUBTOTAL", None));
        self.boton_buscar_producto_facturar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR PRODUCTO", None))
        self.boton_facturar.setText(QCoreApplication.translate("MainWindow", u"FACTURAR", None))
        self.line_nombre_facturar.setText("")
        self.line_nombre_facturar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.label_total.setText(QCoreApplication.translate("MainWindow", u"TOTAL EN DOLARES:", None))
        self.line_cedula_facturar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEDULA", None))
        self.combo_nacionalidad_facturar.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.combo_nacionalidad_facturar.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))

        self.boton_buscar_cliente_facturar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.label_total_iva.setText(QCoreApplication.translate("MainWindow", u"TOTAL + IVA (16%): ", None))
        self.label_iva.setText(QCoreApplication.translate("MainWindow", u"IVA (16%):", None))
        self.line_bproducto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.combo_buscar_bproducto.setItemText(0, QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.combo_buscar_bproducto.setItemText(1, QCoreApplication.translate("MainWindow", u"ID", None))

        ___qtablewidgetitem5 = self.table_productos.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem6 = self.table_productos.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None));
        ___qtablewidgetitem7 = self.table_productos.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"DESCRIPCI\u00d3N", None));
        ___qtablewidgetitem8 = self.table_productos.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"PRECIO", None));
        self.botont_rehacer_cierre.setText(QCoreApplication.translate("MainWindow", u"REHACER CIERRE", None))
        self.label_bs_cierre.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.boton_realizar_cierre.setText(QCoreApplication.translate("MainWindow", u"REALIZAR CIERRE", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TOTAL BS:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TOTAL COP:", None))
        self.boton_buscar_cierre.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.label_cop_cierre.setText(QCoreApplication.translate("MainWindow", u"0", None))
        ___qtablewidgetitem9 = self.table_facturas_cierre.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"FACTURA", None));
        ___qtablewidgetitem10 = self.table_facturas_cierre.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"CEDULA", None));
        ___qtablewidgetitem11 = self.table_facturas_cierre.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"BS", None));
        ___qtablewidgetitem12 = self.table_facturas_cierre.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"COP", None));
        ___qtablewidgetitem13 = self.table_facturas_cierre.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"DOLAR", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TOTAL DOLARES:", None))
        self.label_dolar_cierre.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.boton_configurar_bd.setText(QCoreApplication.translate("MainWindow", u"CONFIGURAR BASE DE DATOS", None))
        self.boton_registrar_usuarios.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR USUARIOS", None))
        self.boton_v_cambiar_usuarios.setText(QCoreApplication.translate("MainWindow", u"CAMBIAR USUARIOS", None))
        self.boton_actualizar_ecliente.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.line_nombre_ecliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.line_telefono_ecliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONO", None))
        self.line_apellido_ecliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"APELLIDO", None))
        self.combo_nacionalidad_ecliente.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.combo_nacionalidad_ecliente.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))

        self.line_cedula_ecliente.setText("")
        self.line_cedula_ecliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEDULA", None))
        self.boton_buscar_ecliente.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.text_descripcion_ecliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DIRECCI\u00d3N (OPCIONAL)", None))
        self.boton_borrar_ecliente.setText(QCoreApplication.translate("MainWindow", u"BORRAR", None))
        self.line_nombre_rproducto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE PRODUCTO", None))
        self.text_descripcion_rproducto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DESCRIPCI\u00d3N DEL PRODUCTO (OPCIONAL)", None))
        self.label_precio.setText(QCoreApplication.translate("MainWindow", u"PRECI\u00d3 EN DOLARES:", None))
        self.boton_registrar_rproducto.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.logo.setText("")
        self.boton_v_facturar.setText(QCoreApplication.translate("MainWindow", u"FACTURAR", None))
        self.boton_v_productos.setText(QCoreApplication.translate("MainWindow", u"PRODUCTOS", None))
        self.boton_v_divisas.setText(QCoreApplication.translate("MainWindow", u"DIVISAS", None))
        self.boton_v_registar_productos.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR\n"
"PRODUCTOS", None))
        self.boton_v_registrar_clientes.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR\n"
"CLIENTES", None))
        self.boton_v_editar_clientes.setText(QCoreApplication.translate("MainWindow", u"EDITAR\n"
"CLIENTES", None))
        self.boton_v_editar_facturas.setText(QCoreApplication.translate("MainWindow", u"EDITAR\n"
"FACTURAS", None))
        self.boton_v_cierre.setText(QCoreApplication.translate("MainWindow", u"CIERRE", None))
        self.boton_v_data.setText(QCoreApplication.translate("MainWindow", u"DATA", None))
        self.boton_v_configuracion.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACI\u00d3N", None))
        self.boton_v_cerrar_sesion.setText(QCoreApplication.translate("MainWindow", u"CERRAR SESI\u00d3N", None))
    # retranslateUi

