from PyQt6.QtWidgets import QWidget
from PyQt6 import uic


File_Qt = "view/Home.ui"


class LoginControl(QWidget):
    def __init__(self) -> None:
        super(LoginControl, self).__init__()
        uic.loadUi(File_Qt, self)
