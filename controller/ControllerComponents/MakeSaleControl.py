from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

File_Qt = "view/components/Sell.ui"


class MakeSaleControl(QWidget):
    def __init__(self) -> None:
        super(MakeSaleControl, self).__init__()
        uic.loadUi(File_Qt, self)
