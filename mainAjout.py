
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ajout import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None): 
        QMainWindow.__init__(self)
        # print("MainWindow initialized")  # Ajoutez cette ligne
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()  # Utilisez la classe MainWindow définie
    main_window.show()
    sys.exit(app.exec_())

