# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_principal.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
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
"#widget_lateral QPushButton{\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(220, 253, 255);\n"
"	width: 100%;\n"
"	padding: 1em 8px;\n"
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
        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_2.addWidget(self.pushButton_6)


        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignLeft)

        self.label = QLabel(self.widget_superior)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMaximumSize(QSize(80, 80))
        self.label.setPixmap(QPixmap(u"../images/logo.png"))
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
        self.pushButton_2 = QPushButton(self.widget_lateral)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.widget_lateral)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.widget_lateral)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.verticalLayout.addWidget(self.pushButton_3)


        self.contenedor_widgets.addWidget(self.widget_lateral, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.stacked_widget = QStackedWidget(self.contenedor_principal)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stacked_widget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stacked_widget.addWidget(self.page_2)

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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

