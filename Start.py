from PyQt6.QtWidgets import QApplication
from controller.MainLogin import MainLogin
from controller.MainWindow import MainWindow
import sys

App = QApplication(sys.argv)
App.setStyle("Fusion")

W = MainWindow()
W.show()

App.exec()
