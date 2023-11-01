
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ajout import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None): 
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # APPLY JSON STYLESHEET
        # self = QMainWindow class  
        # self.ui = Ui_MainWindow / user interface class
        # SHOW WINDOW
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()  
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())

