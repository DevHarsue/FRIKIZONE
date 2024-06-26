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
    QDateEdit, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

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
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
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
        self.boton_v_cierre.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.boton_v_cierre)

        self.boton_v_configuracion = QPushButton(self.widget_superior)
        self.boton_v_configuracion.setObjectName(u"boton_v_configuracion")
        self.boton_v_configuracion.setCursor(QCursor(Qt.PointingHandCursor))

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
        self.logo.setPixmap(QPixmap(u"images/logo.png"))
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
"QDoubleSpinBox, QSpinBox,QDateEd"
                        "it {\n"
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
" bac"
                        "kground: rgb(0, 255, 255);\n"
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
        self.frame_11 = QFrame(self.vista_divisas)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background:transparent;")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_11)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_2 = QWidget(self.frame_11)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(580, 417))
        self.verticalLayout_19 = QVBoxLayout(self.widget_2)
        self.verticalLayout_19.setSpacing(35)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 30, 0, 50)
        self.label_31 = QLabel(self.widget_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(320, 50))
        self.label_31.setMaximumSize(QSize(320, 50))
        self.label_31.setStyleSheet(u"font: 26pt \"Sylfaen\";\n"
"color: rgb(21, 255, 255);")

        self.verticalLayout_19.addWidget(self.label_31, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_13 = QFrame(self.widget_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(250, 200))
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_20 = QVBoxLayout(self.frame_13)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(20, 5, 20, 40)
        self.label_32 = QLabel(self.frame_13)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font: 12pt \"Sylfaen\";")

        self.verticalLayout_20.addWidget(self.label_32, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_3 = QComboBox(self.frame_13)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(28, 40))
        self.comboBox_3.setMaximumSize(QSize(160, 40))
        self.comboBox_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_3.setStyleSheet(u"color:white;\n"
"border-bottom: 1px solid white;")

        self.verticalLayout_20.addWidget(self.comboBox_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_33 = QLabel(self.frame_13)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font: 12pt \"Sylfaen\";")

        self.verticalLayout_20.addWidget(self.label_33, 0, Qt.AlignmentFlag.AlignHCenter)

        self.doubleSpinBox_11 = QDoubleSpinBox(self.frame_13)
        self.doubleSpinBox_11.setObjectName(u"doubleSpinBox_11")
        self.doubleSpinBox_11.setMinimumSize(QSize(137, 40))
        self.doubleSpinBox_11.setMaximumSize(QSize(150, 40))

        self.verticalLayout_20.addWidget(self.doubleSpinBox_11, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_19.addWidget(self.frame_13, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_15 = QPushButton(self.widget_2)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(210, 30))
        self.pushButton_15.setMaximumSize(QSize(192, 30))
        self.pushButton_15.setStyleSheet(u"font: 12pt \"Sylfaen\";")

        self.verticalLayout_19.addWidget(self.pushButton_15, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_21.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_11, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stacked_widget.addWidget(self.vista_divisas)
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
        self.vista_actualizar_productos = QWidget()
        self.vista_actualizar_productos.setObjectName(u"vista_actualizar_productos")
        self.verticalLayout_15 = QVBoxLayout(self.vista_actualizar_productos)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.vista_actualizar_productos)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background:Transparent;")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_8)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget = QWidget(self.frame_8)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(580, 417))
        self.widget.setStyleSheet(u"background: transparent")
        self.gridLayout_17 = QGridLayout(self.widget)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setHorizontalSpacing(0)
        self.gridLayout_17.setVerticalSpacing(15)
        self.gridLayout_17.setContentsMargins(5, 20, 5, 40)
        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(320, 50))
        self.label_22.setMaximumSize(QSize(320, 50))
        self.label_22.setStyleSheet(u"font: 26pt \"Sylfaen\";\n"
"color: rgb(21, 255, 255);")

        self.gridLayout_17.addWidget(self.label_22, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_12 = QPushButton(self.widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(210, 30))
        self.pushButton_12.setMaximumSize(QSize(192, 30))
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet(u"font: 12pt \"Sylfaen\";")

        self.gridLayout_17.addWidget(self.pushButton_12, 3, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.frame_9 = QFrame(self.widget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(300, 200))
        self.frame_9.setMaximumSize(QSize(300, 250))
        self.gridLayout_18 = QGridLayout(self.frame_9)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(10)
        self.gridLayout_18.setVerticalSpacing(0)
        self.gridLayout_18.setContentsMargins(0, 12, 0, 12)
        self.label_23 = QLabel(self.frame_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 40))
        self.label_23.setMaximumSize(QSize(16777215, 40))
        self.label_23.setStyleSheet(u"font: 12pt \"Sylfaen\";")

        self.gridLayout_18.addWidget(self.label_23, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.lineEdit_12 = QLineEdit(self.frame_9)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(172, 40))
        self.lineEdit_12.setMaximumSize(QSize(150, 40))
        self.lineEdit_12.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.gridLayout_18.addWidget(self.lineEdit_12, 0, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.frame_9)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")
        self.doubleSpinBox_8.setMinimumSize(QSize(137, 40))
        self.doubleSpinBox_8.setMaximumSize(QSize(150, 40))
        self.doubleSpinBox_8.setStyleSheet(u"")

        self.gridLayout_18.addWidget(self.doubleSpinBox_8, 1, 1, 1, 1)

        self.label_24 = QLabel(self.frame_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 40))
        self.label_24.setMaximumSize(QSize(16777215, 40))
        self.label_24.setStyleSheet(u"font: 12pt \"Sylfaen\";")

        self.gridLayout_18.addWidget(self.label_24, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_23.raise_()
        self.doubleSpinBox_8.raise_()
        self.label_24.raise_()
        self.lineEdit_12.raise_()

        self.gridLayout_17.addWidget(self.frame_9, 1, 0, 1, 1)


        self.verticalLayout_16.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_15.addWidget(self.frame_8)

        self.stacked_widget.addWidget(self.vista_actualizar_productos)
        self.vista_facturar = QWidget()
        self.vista_facturar.setObjectName(u"vista_facturar")
        self.verticalLayout_13 = QVBoxLayout(self.vista_facturar)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_total = QLabel(self.vista_facturar)
        self.label_total.setObjectName(u"label_total")

        self.gridLayout_4.addWidget(self.label_total, 4, 0, 1, 2)

        self.line_apellido_facturar = QLineEdit(self.vista_facturar)
        self.line_apellido_facturar.setObjectName(u"line_apellido_facturar")
        self.line_apellido_facturar.setEnabled(False)
        self.line_apellido_facturar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.line_apellido_facturar, 1, 2, 1, 1)

        self.boton_buscar_producto_facturar = QPushButton(self.vista_facturar)
        self.boton_buscar_producto_facturar.setObjectName(u"boton_buscar_producto_facturar")
        self.boton_buscar_producto_facturar.setMinimumSize(QSize(140, 0))
        self.boton_buscar_producto_facturar.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.boton_buscar_producto_facturar, 2, 1, 1, 1)

        self.line_nombre_facturar = QLineEdit(self.vista_facturar)
        self.line_nombre_facturar.setObjectName(u"line_nombre_facturar")
        self.line_nombre_facturar.setEnabled(False)
        self.line_nombre_facturar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.line_nombre_facturar, 1, 0, 1, 1)

        self.line_cedula_facturar = QLineEdit(self.vista_facturar)
        self.line_cedula_facturar.setObjectName(u"line_cedula_facturar")

        self.gridLayout_4.addWidget(self.line_cedula_facturar, 0, 1, 1, 1)

        self.combo_nacionalidad_facturar = QComboBox(self.vista_facturar)
        self.combo_nacionalidad_facturar.addItem("")
        self.combo_nacionalidad_facturar.addItem("")
        self.combo_nacionalidad_facturar.setObjectName(u"combo_nacionalidad_facturar")

        self.gridLayout_4.addWidget(self.combo_nacionalidad_facturar, 0, 0, 1, 1)

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
        self.double_bs_facturar.setMaximum(999999999.990000009536743)

        self.gridLayout_5.addWidget(self.double_bs_facturar, 0, 2, 1, 2)

        self.spin_cop_facturar = QSpinBox(self.vista_facturar)
        self.spin_cop_facturar.setObjectName(u"spin_cop_facturar")
        self.spin_cop_facturar.setMinimum(0)
        self.spin_cop_facturar.setMaximum(999999999)
        self.spin_cop_facturar.setSingleStep(1000)
        self.spin_cop_facturar.setDisplayIntegerBase(10)

        self.gridLayout_5.addWidget(self.spin_cop_facturar, 0, 4, 1, 2)


        self.gridLayout_4.addLayout(self.gridLayout_5, 5, 0, 1, 3)

        self.boton_buscar_cliente_facturar = QPushButton(self.vista_facturar)
        self.boton_buscar_cliente_facturar.setObjectName(u"boton_buscar_cliente_facturar")
        icon1 = QIcon(QIcon.fromTheme(u"system-search"))
        self.boton_buscar_cliente_facturar.setIcon(icon1)

        self.gridLayout_4.addWidget(self.boton_buscar_cliente_facturar, 0, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

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

        self.boton_facturar = QPushButton(self.vista_facturar)
        self.boton_facturar.setObjectName(u"boton_facturar")
        self.boton_facturar.setMinimumSize(QSize(140, 0))
        self.boton_facturar.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.boton_facturar, 6, 1, 1, 1)


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
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_6.addWidget(self.pushButton_3, 8, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_total_dolares_cierre = QLabel(self.vista_cierre)
        self.label_total_dolares_cierre.setObjectName(u"label_total_dolares_cierre")

        self.gridLayout_6.addWidget(self.label_total_dolares_cierre, 6, 0, 1, 1)

        self.pushButton = QPushButton(self.vista_cierre)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

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
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

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
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FRIKIZONE", None))
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
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Actualizar Divisas</p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Tipo de Divisa", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"COP", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"BS", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"USD", None))

        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Tasa del d\u00eda", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
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
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Actualizar Productos", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Nombre del Producto", None))
        self.lineEdit_12.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Precio del Producto", None))
        self.label_total.setText(QCoreApplication.translate("MainWindow", u"TOTAL EN DOLARES:", None))
        self.line_apellido_facturar.setText("")
        self.line_apellido_facturar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"APELLIDO", None))
        self.boton_buscar_producto_facturar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR PRODUCTO", None))
        self.line_nombre_facturar.setText("")
        self.line_nombre_facturar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.line_cedula_facturar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEDULA", None))
        self.combo_nacionalidad_facturar.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.combo_nacionalidad_facturar.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))

        self.label_cop_facturar.setText(QCoreApplication.translate("MainWindow", u"Valor COP:", None))
        self.label_dolar.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_dolar_facturar.setText(QCoreApplication.translate("MainWindow", u"Valor $:", None))
        self.label_bs_facturar.setText(QCoreApplication.translate("MainWindow", u"Valor BS:", None))
        self.label_bs.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_cop.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.boton_buscar_cliente_facturar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
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
        self.boton_facturar.setText(QCoreApplication.translate("MainWindow", u"FACTURAR", None))
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

