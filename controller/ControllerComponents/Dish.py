from PyQt6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from PyQt6 import uic

from model.Dish.Dish_DAO import Dish_DAO
from model.Dish.Dish import Dish

File_Qt = "view/components/Dish.ui"


class Dish(QWidget):
    def __init__(self) -> None:
        super(Dish, self).__init__()
        uic.loadUi(File_Qt, self)

        self.Table.horizontalHeader().setStretchLastSection(True)
        self.Table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.LoadData()
        # self.Table.cellClicked.connect(self.GetText)
        self.BtnAdd.clicked.connect(self.RegisterDish)

    def LoadData(self):
        list = Dish_DAO.SelectAll()
        for x in list:
            self.AddTableWidget(x)

    def ClearField(self):
        self.InputName.clear()
        self.InputDescription.clear()
        self.InputPrice.clear()
        self.AlertDish.clear()

    def RegisterDish(self):
        Name = self.InputName.text()
        Description = self.InputDescription.text()
        Price = self.InputPrice.text()
        Status = self.InputStatus.currentText()

        New = Dish(-1, Name, Description, Price, Status)
        Id = Dish_DAO.AddDAO(New)
        New.Id = Id
        self.AddTableWidget(New)

    def GetText(self):
        Line = self.Table.currentRow()

        self.InputName.setText(self.Table.item(Line, 1).text())
        self.InputDescription.setText(self.Table.item(Line, 2).text())
        self.InputPrice.setText(self.Table.item(Line, 3).text())

    def AddTableWidget(self, w: Dish):
        Line = self.Table.rowCount()
        self.Table.insertRow(Line)

        Id = QTableWidgetItem(str(w.Id))
        Name = QTableWidgetItem(w.Name)
        Description = QTableWidgetItem(w.Description)
        Price = QTableWidgetItem(w.Price)
        Status = QTableWidgetItem(w.Status)

        self.Table.setItem(Line, 0, Id)
        self.Table.setItem(Line, 1, Name)
        self.Table.setItem(Line, 2, Description)
        self.Table.setItem(Line, 3, Price)
        self.Table.setItem(Line, 4, Status)
