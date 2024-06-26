# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'question.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Question(object):
    def setupUi(self, Question):
        if not Question.objectName():
            Question.setObjectName(u"Question")
        Question.resize(370, 79)
        Question.setMaximumSize(QSize(370, 80))
        icon = QIcon()
        icon.addFile(u"images/zone.ico", QSize(), QIcon.Normal, QIcon.Off)
        Question.setWindowIcon(icon)
        Question.setStyleSheet(u"*{\n"
"	font-size: 12px;\n"
"	font-family: Rockwell;\n"
"}\n"
"\n"
"#Question{background: url(\"images/fondo_messagebox.png\")}\n"
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
        self.verticalLayout = QVBoxLayout(Question)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.centralwidget = QWidget(Question)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.centralwidget)

        QWidget.setTabOrder(self.pushButton_2, self.pushButton)

        self.retranslateUi(Question)

        QMetaObject.connectSlotsByName(Question)
    # setupUi

    def retranslateUi(self, Question):
        Question.setWindowTitle(QCoreApplication.translate("Question", u"title", None))
        self.pushButton.setText(QCoreApplication.translate("Question", u"SI", None))
        self.pushButton_2.setText(QCoreApplication.translate("Question", u"NO", None))
        self.label.setText(QCoreApplication.translate("Question", u"xds", None))
    # retranslateUi

