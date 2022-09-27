from PyQt6.QtWidgets import QApplication
from controller.MainWindow import MainWindow
from controller.MainLogin import MainLogin
import sys

App = QApplication(sys.argv)
App.setStyle("Fusion")

x = 1
if x == 1:
    c = MainLogin()
    c.show()
else:
    janela = MainWindow()
    janela.show()

App.exec()
