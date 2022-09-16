from PyQt6.QtWidgets import QWidget, QHeaderView
from PyQt6 import uic

File_Qt = "view/components/Menu.ui"


class Menu(QWidget):
    def __init__(self) -> None:
        super(Menu, self).__init__()
        uic.loadUi(File_Qt, self)

        self.Table.horizontalHeader().setStretchLastSection(True)
        self.Table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
