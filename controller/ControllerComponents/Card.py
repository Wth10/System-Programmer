from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

from model.Menu.Menu import Menu

File_Qt = "view/components/Card.ui"


class Card(QWidget):
    def __init__(self, x: Menu):
        super(Card, self).__init__()
        uic.loadUi(File_Qt, self)
        self.x = x

        self.Load()

    def Load(self):
        self.Name.setText(f"{self.x.Name}")
        self.Description.setText(f"{self.x.Description}")
        self.Price.setText(f"{self.x.Price}")
