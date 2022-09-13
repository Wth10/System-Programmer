from PyQt6.QtWidgets import QWidget
from PyQt6 import uic


File_Qt = "view/layout/Cadastro.ui"


class ControllRegistration(QWidget):
    def __init__(self) -> None:
        super(ControllRegistration, self).__init__()
        uic.loadUi(File_Qt, self)
