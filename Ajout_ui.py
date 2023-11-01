# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ajout.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(513, 313)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 471, 271))
        self.frame.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLabel{\n"
"color: #FF6600;\n"
"}\n"
"\n"
"QLabel#label{\n"
"color:#000;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border:none;\n"
"border-bottom: 2px solid #cccccc;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border-bottom: 2px solid #FF6600;\n"
"}")
        self.btnAnnuler = QPushButton(self.frame)
        self.btnAnnuler.setObjectName(u"btnAnnuler")
        self.btnAnnuler.setGeometry(QRect(9, 240, 75, 31))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(9)
        self.btnAnnuler.setFont(font)
        self.btnAnnuler.setStyleSheet(u"border: none;")
        self.btnAjouter = QPushButton(self.frame)
        self.btnAjouter.setObjectName(u"btnAjouter")
        self.btnAjouter.setGeometry(QRect(70, 240, 75, 31))
        self.btnAjouter.setFont(font)
        self.btnAjouter.setStyleSheet(u"border: none;")
        self.labelTexte = QLabel(self.frame)
        self.labelTexte.setObjectName(u"labelTexte")
        self.labelTexte.setGeometry(QRect(10, 10, 111, 31))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.labelTexte.setFont(font1)
        self.labelTexte.setStyleSheet(u"color:black;")
        self.labelTexte.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 120, 201, 39))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelTelephone = QLabel(self.layoutWidget)
        self.labelTelephone.setObjectName(u"labelTelephone")

        self.verticalLayout.addWidget(self.labelTelephone)

        self.inputTelephone = QLineEdit(self.layoutWidget)
        self.inputTelephone.setObjectName(u"inputTelephone")
        self.inputTelephone.setStyleSheet(u"border-radius:none;")

        self.verticalLayout.addWidget(self.inputTelephone)

        self.layoutWidget_2 = QWidget(self.frame)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 70, 201, 39))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelNom = QLabel(self.layoutWidget_2)
        self.labelNom.setObjectName(u"labelNom")

        self.verticalLayout_2.addWidget(self.labelNom)

        self.inputNom = QLineEdit(self.layoutWidget_2)
        self.inputNom.setObjectName(u"inputNom")
        self.inputNom.setStyleSheet(u"border-radius:none;")

        self.verticalLayout_2.addWidget(self.inputNom)

        self.layoutWidget_5 = QWidget(self.frame)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(240, 170, 201, 39))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.labelDescription = QLabel(self.layoutWidget_5)
        self.labelDescription.setObjectName(u"labelDescription")

        self.verticalLayout_5.addWidget(self.labelDescription)

        self.inputDescription = QLineEdit(self.layoutWidget_5)
        self.inputDescription.setObjectName(u"inputDescription")
        self.inputDescription.setStyleSheet(u"border-radius:none;")

        self.verticalLayout_5.addWidget(self.inputDescription)

        self.layoutWidget_6 = QWidget(self.frame)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(30, 170, 201, 39))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.labelActivite = QLabel(self.layoutWidget_6)
        self.labelActivite.setObjectName(u"labelActivite")

        self.verticalLayout_6.addWidget(self.labelActivite)

        self.inputActivite = QLineEdit(self.layoutWidget_6)
        self.inputActivite.setObjectName(u"inputActivite")
        self.inputActivite.setStyleSheet(u"border-radius:none;")

        self.verticalLayout_6.addWidget(self.inputActivite)

        self.layoutWidget_3 = QWidget(self.frame)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(240, 120, 201, 39))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelDate = QLabel(self.layoutWidget_3)
        self.labelDate.setObjectName(u"labelDate")

        self.verticalLayout_3.addWidget(self.labelDate)

        self.inputDate = QLineEdit(self.layoutWidget_3)
        self.inputDate.setObjectName(u"inputDate")
        self.inputDate.setStyleSheet(u"border-radius:none;")

        self.verticalLayout_3.addWidget(self.inputDate)

        self.layoutWidget_4 = QWidget(self.frame)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(240, 70, 201, 39))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.labelEmail = QLabel(self.layoutWidget_4)
        self.labelEmail.setObjectName(u"labelEmail")

        self.verticalLayout_4.addWidget(self.labelEmail)

        self.inputEmail = QLineEdit(self.layoutWidget_4)
        self.inputEmail.setObjectName(u"inputEmail")
        self.inputEmail.setStyleSheet(u"border-radius:none;")

        self.verticalLayout_4.addWidget(self.inputEmail)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnAnnuler.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.btnAjouter.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.labelTexte.setText(QCoreApplication.translate("MainWindow", u"Ajout Prospect", None))
        self.labelTelephone.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9phone*", None))
        self.labelNom.setText(QCoreApplication.translate("MainWindow", u"Nom*", None))
        self.labelDescription.setText(QCoreApplication.translate("MainWindow", u"Description*", None))
        self.labelActivite.setText(QCoreApplication.translate("MainWindow", u"Activit\u00e9*", None))
        self.labelDate.setText(QCoreApplication.translate("MainWindow", u"Date*", None))
        self.labelEmail.setText(QCoreApplication.translate("MainWindow", u"Email*", None))
    # retranslateUi

