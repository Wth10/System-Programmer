from PyQt6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from PyQt6 import uic

from model.Menu.Menu import Menu
from model.Menu.Menu_DAO import Menu_DAO

from controller.ControllerComponents.Card import Card

File_Qt = "view/components/Menu.ui"
from random import randint


class MenuControl(QWidget):
    def __init__(self) -> None:
        super(MenuControl, self).__init__()
        uic.loadUi(File_Qt, self)

        self.Alert()
        self.Update.clicked.connect(self.UpdatePage)

    def Alert(self):
        PlateCount = Menu_DAO.PlateCount()

        if PlateCount == 0:
            self.AlertMenu.clear()
            self.AlertMenu.setText(f"Nenhum Prato Cadastrado!!")
        else:
            self.AlertMenu.clear()
            self.AlertMenu.setText(f"Nº {PlateCount} Platos Cadastrado")

    def UpdatePage(self, w: Menu):
        self.ClearCard()

        Name = Menu_DAO.getName()
        Price = Menu_DAO.getPrice()
        Description = Menu_DAO.getDescription()
        for x in range(0, len(Name)):
            w = Menu(
                f"{Name[x][0]}",
                f"Preço: R$ {Price[x][0]}",
                f"Descrição: {Description[x][0]}",
            )

            CardX = Card(w)
            self.CardConteiner.addWidget(CardX)

    def ClearCard(self):
        for x in range(self.CardConteiner.count()):
            CardX = self.CardConteiner.itemAt(x).widget()
            CardX.hide()
