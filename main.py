############################################################
## Method - 1 [Convert UI Design into Python Code]
############################################################

from PySide2 import QtWidgets
from ui_mainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()




############################################################
## Method - 2 [Load .ui file in your Python Program]
############################################################

from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader


loader = QUiLoader()
app = QtWidgets.QApplication([])
window = loader.load('mainWIndow.ui', None)
window.show()
app.exec_()
