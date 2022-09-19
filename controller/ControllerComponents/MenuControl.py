from PyQt6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from PyQt6 import uic

from model.Menu.Menu import Menu
from model.Menu.Menu_DAO import Menu_DAO

File_Qt = "view/components/Menu.ui"


class MenuControl(QWidget):
    def __init__(self) -> None:
        super(MenuControl, self).__init__()
        uic.loadUi(File_Qt, self)

        self.Table.horizontalHeader().setStretchLastSection(True)
        self.Table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.LoadData()
        self.Alert()

    def LoadData(self):
        list = Menu_DAO.SpecificSelection()
        for x in list:
            self.AddTableWidget(x)

    def Alert(self):
        PlateCount = Menu_DAO.PlateCount()

        if PlateCount == 0:
            self.AlertMenu.setText(f"Nenhum Prato Cadastrado!!")
        else:
            None

    def AddTableWidget(self, w: Menu):
        Line = self.Table.rowCount()
        self.Table.insertRow(Line)

        Name = QTableWidgetItem(w.Name)
        Description = QTableWidgetItem(w.Description)
        Price = QTableWidgetItem(f"R$ {w.Price}")

        self.Table.setItem(Line, 0, Name)
        self.Table.setItem(Line, 1, Description)
        self.Table.setItem(Line, 2, Price)
