
import os
import sys

from Principal_Larissa_ui import *

import os

# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
# INITIALIZE APP SETTINGS
settings = QSettings()

## MAIN WINDOW CLASS

class MainWindow(QMainWindow):
    def __init__(self, parent=None): 
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # APPLY JSON STYLESHEET
        # self = QMainWindow class  
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        # SHOW WINDOW
        self.show()

      
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################