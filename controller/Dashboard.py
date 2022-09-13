from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

File_Qt = "view/Dashboard.ui"


class Dashboard(QMainWindow):
    def __init__(self) -> None:
        super(Dashboard, self).__init__()
        uic.loadUi(File_Qt, self)
