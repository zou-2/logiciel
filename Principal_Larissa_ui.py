# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Principal_Larissa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sqlite3
import subprocess
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

from Custom_Widgets.Widgets import QCustomStackedWidget

import os
import Session
# from mainAjout import *


# from mainAjout import MainWindow


# Obtenez le chemin absolu du répertoire du script
script_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_dir, "LARISSA.db")


import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(892, 489)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.background = QFrame(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setStyleSheet(u"#background{\n"
"	background-color : white;\n"
"	\n"
"}")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.background)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header = QFrame(self.background)
        self.Header.setObjectName(u"Header")
        self.Header.setMinimumSize(QSize(0, 28))
        self.Header.setStyleSheet(u"*{\n"
"	color: black;\n"
"	background: white;\n"
"	border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel{\n"
"	color:black;\n"
"	border: none;\n"
"}")
        self.Header.setFrameShape(QFrame.StyledPanel)
        self.Header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 2, 0, 0)
        self.frame = QFrame(self.Header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_2 = QFrame(self.Header)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(20, 20))
        self.pushButton_4.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/icons/UI/trending-up2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setIndent(6)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.Header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/UI/minusBlack.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u":/icons/UI/squareBlack.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon3 = QIcon()
        icon3.addFile(u":/icons/UI/xBlack.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.Header, 0, Qt.AlignTop)

        self.Main = QFrame(self.background)
        self.Main.setObjectName(u"Main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Main.sizePolicy().hasHeightForWidth())
        self.Main.setSizePolicy(sizePolicy1)
        self.Main.setStyleSheet(u"")
        self.Main.setFrameShape(QFrame.StyledPanel)
        self.Main.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.Main)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 171, 441))
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setWeight(50)
        self.frame_4.setFont(font1)
        self.frame_4.setStyleSheet(u"background-color: #1e2b34;\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.btnDeconnexion = QPushButton(self.frame_4)
        self.btnDeconnexion.setObjectName(u"btnDeconnexion")
        self.btnDeconnexion.setGeometry(QRect(5, 150, 121, 26))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.btnDeconnexion.setFont(font2)
        self.btnDeconnexion.setStyleSheet(u"\n"
"*:hover{\n"
"	margin-left: 4px;\n"
"	\n"
"	\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/UI/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDeconnexion.setIcon(icon4)
        self.btnDeconnexion.setIconSize(QSize(20, 20))
        self.btnTableau = QPushButton(self.frame_4)
        self.btnTableau.setObjectName(u"btnTableau")
        self.btnTableau.setGeometry(QRect(5, 30, 141, 26))
        font3 = QFont()
        font3.setPointSize(10)
        self.btnTableau.setFont(font3)
        self.btnTableau.setStyleSheet(u"\n"
"\n"
"*:hover{\n"
"	margin-left: 4px;\n"
"	\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/UI/table.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnTableau.setIcon(icon5)
        self.btnTableau.setIconSize(QSize(20, 20))
        self.btnProspects = QPushButton(self.frame_4)
        self.btnProspects.setObjectName(u"btnProspects")
        self.btnProspects.setGeometry(QRect(10, 90, 121, 28))
        self.btnProspects.setFont(font3)
        self.btnProspects.setStyleSheet(u"*{\n"
"margin-left: -25px;\n"
"}\n"
"*:hover{\n"
"	margin-left: -21px;\n"
"	\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/UI/trending-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnProspects.setIcon(icon6)
        self.btnProspects.setIconSize(QSize(18, 18))
        self.btnProspects.setAutoRepeatInterval(100)
        self.frame_5 = QFrame(self.Main)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(134, 0, 761, 431))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.mainPage = QCustomStackedWidget(self.frame_5)
        self.mainPage.setObjectName(u"mainPage")
        self.mainPage.setGeometry(QRect(40, 30, 711, 401))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainPage.sizePolicy().hasHeightForWidth())
        self.mainPage.setSizePolicy(sizePolicy2)
        self.mainPage.setStyleSheet(u"\n"
"	background-color: white;\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid white;\n"
"	background: transparent;\n"
"	color: white;\n"
"}")
        self.mainPage.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.btnRecherche = QPushButton(self.page_2)
        self.btnRecherche.setObjectName(u"btnRecherche")
        self.btnRecherche.setGeometry(QRect(130, 50, 101, 31))
        self.btnRecherche.setStyleSheet(u"border-radius: 5px;\n"
"background-color: green;\n"
"color: white;")
        icon7 = QIcon()
        icon7.addFile(u":/icons/UI/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRecherche.setIcon(icon7)
        self.table = QTableWidget(self.page_2)
        if (self.table.columnCount() < 7):
            self.table.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font4);
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(10, 100, 691, 241))
        self.btnAjoutProspect = QPushButton(self.page_2)
        self.btnAjoutProspect.setObjectName(u"btnAjoutProspect")
        self.btnAjoutProspect.setGeometry(QRect(600, 50, 101, 31))
        self.btnAjoutProspect.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(64, 82, 180);\n"
"color:white;")
        self.inputRecherche = QLineEdit(self.page_2)
        self.inputRecherche.setObjectName(u"inputRecherche")
        self.inputRecherche.setGeometry(QRect(250, 50, 331, 31))
        self.inputRecherche.setStyleSheet(u"QLineEdit{\n"
"	color:black;\n"
"	border: 1px dotted black;\n"
"	border-bottom: 2px solid grey;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border-bottom: 2px solid #FF6600;\n"
"}")
        self.btnActualiser = QPushButton(self.page_2)
        self.btnActualiser.setObjectName(u"btnActualiser")
        self.btnActualiser.setGeometry(QRect(10, 50, 101, 31))
        self.btnActualiser.setStyleSheet(u"border-radius: 5px;\n"
"background-color: grey;\n"
"color: white;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/UI/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnActualiser.setIcon(icon8)
        self.mainPage.addWidget(self.page_2)
        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(610, 0, 51, 31))
        self.pushButton_5.setStyleSheet(u"background-color: white;\n"
"border:none;")
        icon9 = QIcon()
        icon9.addFile(u":/icons/UI/userBlack.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon9)
        self.pushButton_5.setIconSize(QSize(20, 20))
        self.labelUserConnected = QLabel(self.frame_5)
        self.labelUserConnected.setObjectName(u"labelUserConnected")
        self.labelUserConnected.setGeometry(QRect(656, 10, 91, 16))
        self.frame_5.raise_()
        self.frame_4.raise_()

        self.verticalLayout.addWidget(self.Main)

        self.Footer = QFrame(self.background)
        self.Footer.setObjectName(u"Footer")
        self.Footer.setMinimumSize(QSize(0, 25))
        self.Footer.setMaximumSize(QSize(16777215, 25))
        self.Footer.setSizeIncrement(QSize(0, 0))
        self.Footer.setStyleSheet(u"background-color: white;\n"
"")
        self.Footer.setFrameShape(QFrame.StyledPanel)
        self.Footer.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.Footer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(570, 0, 24, 22))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.Footer)


        self.horizontalLayout.addWidget(self.background)
        
        
        
        self.btnActualiser.clicked.connect(self.showTableData)
        self.btnDeconnexion.clicked.connect(MainWindow.close)
        self.btnRecherche.clicked.connect(self.search)
        self.showTableData()
        
        
        
        self.btnAjoutProspect.clicked.connect(self.appelAjoutProspect)
        

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPage.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    
    
    def appelAjoutProspect(self):
        subprocess.Popen(["python", "mainAjout.py"])   
        # print("tafiditra ato")
        # prospect_window = MainWindow()
        
        # # prospect_window.show()
        # print("tonga et ambany")
        
        # # MainWindow.close()
    
    def user(self):
        UserPrenom = Session.user_data['prenom']
        return UserPrenom
    
    def search(self):
        # print("test:",self.inputRecherche.text())
        id = self.inputRecherche.text()
       
        for row_number in range(self.table.rowCount()):
            found = False
            for column_number in range(self.table.columnCount()):
                item = self.table.item(row_number, column_number)
                if item and id in item.text():
                    found = True
                    break
            if found:
                self.table.showRow(row_number)
            else:
                self.table.hideRow(row_number)
                
        if self.table.rowCount() == 0:
            QMessageBox.information(self, "Information", "Aucune ligne trouvée avec la recherche : {}".format(id))

        
    def showTableData(self):
        # Connexion à la base de données
        self.inputRecherche.setText("")
        con = sqlite3.connect(database_path)
        cur = con.cursor()
        cur.execute("select * from Prospects")
        con.commit()
        RqtResult = cur.fetchall()
        
        self.table.clearContents()
        self.table.setRowCount(0)
        
        for row_number, row_data in enumerate(RqtResult):
            self.table.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                self.table.setItem(row_number, column_number, QTableWidgetItem(item))
                
        con.close()
    
    
    
    

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_4.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Prospects", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText("")
        self.btnDeconnexion.setText(QCoreApplication.translate("MainWindow", u"D\u00e9connexion", None))
        self.btnTableau.setText(QCoreApplication.translate("MainWindow", u"Tableau de bord", None))
        self.btnProspects.setText(QCoreApplication.translate("MainWindow", u"Prospects", None))
        self.btnRecherche.setText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l\u00e9phone", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Activit\u00e9", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        self.btnAjoutProspect.setText(QCoreApplication.translate("MainWindow", u"Ajout prostect", None))
        self.inputRecherche.setText("")
        self.btnActualiser.setText(QCoreApplication.translate("MainWindow", u"Actualiser", None))
        self.pushButton_5.setText("")
        self.labelUserConnected.setText(QCoreApplication.translate("MainWindow", self.user(), None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())