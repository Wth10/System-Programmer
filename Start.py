from PyQt6.QtWidgets import QApplication
from controller.MainWindow import MainWindow
from controller.Login import LoginControl
import sys

App = QApplication(sys.argv)
App.setStyle("Fusion")

x = 0
if x == 1:
    c = LoginControl()
    c.show()
else:
    janela = MainWindow()
    janela.show()

App.exec()
