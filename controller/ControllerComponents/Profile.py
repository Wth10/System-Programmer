from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

File_Qt = "view/components/Profile.ui"


class Profile(QWidget):
    def __init__(self) -> None:
        super(Profile, self).__init__()
        uic.loadUi(File_Qt, self)
