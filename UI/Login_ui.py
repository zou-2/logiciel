# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import logo_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(591, 411)
        self.gauche = QWidget(Form)
        self.gauche.setObjectName(u"gauche")
        self.gauche.setEnabled(True)
        self.gauche.setGeometry(QRect(0, 0, 291, 411))
        self.gauche.setStyleSheet(u"background-color: #cececd")
        self.Logo = QLabel(self.gauche)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(60, 110, 151, 141))
        self.copyRight = QLabel(self.gauche)
        self.copyRight.setObjectName(u"copyRight")
        self.copyRight.setGeometry(QRect(90, 370, 111, 31))
        self.droite = QWidget(Form)
        self.droite.setObjectName(u"droite")
        self.droite.setGeometry(QRect(290, 0, 301, 411))
        font = QFont()
        font.setPointSize(8)
        self.droite.setFont(font)
        self.droite.setStyleSheet(u"background-color: #146618;")
        self.connexion = QLabel(self.droite)
        self.connexion.setObjectName(u"connexion")
        self.connexion.setGeometry(QRect(70, 40, 161, 61))
        self.connexion.setStyleSheet(u"color: white;")
        self.user = QLabel(self.droite)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(20, 170, 91, 21))
        self.user.setStyleSheet(u"color: white;")
        self.password = QLabel(self.droite)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(20, 230, 121, 21))
        self.password.setStyleSheet(u"color: white;")
        self.inputUser = QLineEdit(self.droite)
        self.inputUser.setObjectName(u"inputUser")
        self.inputUser.setGeometry(QRect(140, 160, 131, 31))
        self.inputUser.setStyleSheet(u"background-colo: #FFFFFF;\n"
"border:none;\n"
"border-bottom:2px solid #FFFFFF;\n"
"color :white;\n"
"padding-bottom:7px;")
        self.seConnecter = QPushButton(self.droite)
        self.seConnecter.setObjectName(u"seConnecter")
        self.seConnecter.setGeometry(QRect(110, 310, 111, 31))
        font1 = QFont()
        font1.setPointSize(11)
        self.seConnecter.setFont(font1)
        self.seConnecter.setStyleSheet(u"background-color: #00ff00;\n"
"color : white;\n"
"border-radius: 5px;")
        self.inputPswrd = QLineEdit(self.droite)
        self.inputPswrd.setObjectName(u"inputPswrd")
        self.inputPswrd.setGeometry(QRect(140, 220, 131, 31))
        self.inputPswrd.setStyleSheet(u"background-colo: #FFFFFF;\n"
"border:none;\n"
"border-bottom:2px solid #FFFFFF;\n"
"color :white;\n"
"padding-bottom:7px;\n"
"type:password;")
        self.inputPswrd.setEchoMode(QLineEdit.Password)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Logo.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><img src=\":/newPrefix/Pictures/logoCamShoot.png\"/></p></body></html>", None))
        self.copyRight.setText(QCoreApplication.translate("Form", u"Copy Right 2022", None))
        self.connexion.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:26pt;\">Connexion</span></p></body></html>", None))
        self.user.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt;\">Utilisateur</span></p></body></html>", None))
        self.password.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt;\">Mot de passe</span></p></body></html>", None))
        self.inputUser.setPlaceholderText("")
        self.seConnecter.setText(QCoreApplication.translate("Form", u"Se connecter", None))
        self.inputPswrd.setInputMask("")
        self.inputPswrd.setPlaceholderText("")
    # retranslateUi

