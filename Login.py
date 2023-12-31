# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtWidgets import QApplication, QMainWindow,QLineEdit,QAction
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import Session
import sqlite3
import main
import sys 
import os


# Obtenez le chemin absolu du répertoire du script
script_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_dir, "LARISSA.db")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(393, 283)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 351, 241))
        self.widget.setStyleSheet("QWidget{\n"
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
        self.widget.setObjectName("widget")
        self.btnAnnuler = QtWidgets.QPushButton(self.widget)
        self.btnAnnuler.setGeometry(QtCore.QRect(-1, 210, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.btnAnnuler.setFont(font)
        self.btnAnnuler.setStyleSheet("border: none;")
        self.btnAnnuler.setObjectName("btnAnnuler")
        self.btnConfirmer = QtWidgets.QPushButton(self.widget)
        self.btnConfirmer.setGeometry(QtCore.QRect(60, 210, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.btnConfirmer.setFont(font)
        self.btnConfirmer.setStyleSheet("border: none;")
        self.btnConfirmer.setObjectName("btnConfirmer")
        self.labelTexte = QtWidgets.QLabel(self.widget)
        self.labelTexte.setGeometry(QtCore.QRect(0, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelTexte.setFont(font)
        self.labelTexte.setStyleSheet("color:black;")
        self.labelTexte.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTexte.setObjectName("labelTexte")
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setGeometry(QtCore.QRect(50, 140, 261, 39))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelPswrd = QtWidgets.QLabel(self.widget1)
        self.labelPswrd.setObjectName("labelPswrd")
        self.verticalLayout.addWidget(self.labelPswrd)
        self.inputPswrd = QtWidgets.QLineEdit(self.widget1)
        self.inputPswrd.setStyleSheet("border-radius:none;")
        self.inputPswrd.setObjectName("inputPswrd")
        self.verticalLayout.addWidget(self.inputPswrd)
        self.widget2 = QtWidgets.QWidget(self.widget)
        self.widget2.setGeometry(QtCore.QRect(50, 70, 261, 39))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelUser = QtWidgets.QLabel(self.widget2)
        self.labelUser.setObjectName("labelUser")
        self.verticalLayout_2.addWidget(self.labelUser)
        self.inputUser = QtWidgets.QLineEdit(self.widget2)
        self.inputUser.setStyleSheet("border-radius:none;")
        self.inputUser.setObjectName("inputUser")
        self.verticalLayout_2.addWidget(self.inputUser)
        
        
        
        
        
        self.username_label = self.labelUser
        self.password_label = self.labelPswrd
        
        self.username_label.setText("")
        self.password_label.setText("")
        
        self.username_input = self.inputUser
        self.password_input = self.inputPswrd
        
        self.username_input.setPlaceholderText("Utilisateur*")
        self.password_input.setPlaceholderText("Mot de passe*")
        
        self.username_input.setClearButtonEnabled(True)
        self.password_input.setClearButtonEnabled(True)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.btnConfirmer.setEnabled(False)
        
        icon = QIcon(":icons/UI/x2.svg")
        self.username_input.findChildren(QAction)[0].setIcon(icon)
        self.password_input.findChildren(QAction)[0].setIcon(icon)
        
        
        self.username_input.textChanged.connect(self.do_username_label)
        self.password_input.textChanged.connect(self.do_password_label)
        self.inputUser.textChanged.connect(self.checkFields)
        self.inputPswrd.textChanged.connect(self.checkFields)
        self.btnAnnuler.clicked.connect(MainWindow.close)
        self.btnConfirmer.clicked.connect(self.Connexion)
        
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
     
     
    def Connexion(self):
        userName = self.inputUser.text()
        password = self.inputPswrd.text()
         # connexion à la base de données
        con = sqlite3.connect(database_path)
        cur = con.cursor()
        cur.execute("select * from Login")
        
        RqtResult = cur.fetchall()
        
        for user in RqtResult:
            UserBD = user[0]
            PasswordBD = user[1]
            
            
            if ((str(password) == str(PasswordBD)) and (str(UserBD) == str(userName))):
                self.inputUser.setText("")
                self.inputPswrd.setText("")
                user_data = {
                    "prenom": user[3],
                    
                }
                Session.user_data = user_data
                
                self.open_main_window()    
                
                ########################################################################
                ## END===>
                ########################################################################
                con.close()
                return  # Sortez de la boucle après la première correspondance
               
    def open_main_window(self):
         # Créez une instance de la fenêtre principale (MainWindow)
        main_window = main.MainWindow()  
    
        # Affichez la fenêtre principale
        main_window.show()
    
        # Fermez la fenêtre de connexion actuelle
        MainWindow.close()   
        
    def do_username_label(self, text):
        if text:
            self.username_label.setText("Utilisateur*")
        else:
            self.username_label.setText("")
            
            
    def do_password_label(self, text):
        if text:
            self.password_label.setText("Mot de passe*")
        else:
            self.password_label.setText("")
            
            
    def checkFields(self):
        username_text = self.inputUser.text()
        password_text = self.inputPswrd.text()
        enable_button = bool(username_text and password_text)
        self.btnConfirmer.setEnabled(enable_button)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnAnnuler.setText(_translate("MainWindow", "Annuler"))
        self.btnConfirmer.setText(_translate("MainWindow", "Confirmer"))
        self.labelTexte.setText(_translate("MainWindow", "Se connecter à votre compte"))
        self.labelPswrd.setText(_translate("MainWindow", ""))
        self.labelUser.setText(_translate("MainWindow", ""))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
