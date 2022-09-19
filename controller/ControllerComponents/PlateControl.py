from PyQt6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from PyQt6 import uic

from model.Dish.Dish import Dish
from model.Dish.Dish_DAO import Dish_DAO

File_Qt = "view/components/Dish.ui"


class PlateControl(QWidget):
    def __init__(self) -> None:
        super(PlateControl, self).__init__()
        uic.loadUi(File_Qt, self)

        self.Table.horizontalHeader().setStretchLastSection(True)
        self.Table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.LoadData()
        self.Table.cellClicked.connect(self.GetText)
        self.BtnAdd.clicked.connect(self.RegisterDish)
        self.BtnDelete.clicked.connect(self.DeleteDish)

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

        if Name == "" or Description == "" or Price == "" or Status == "":
            self.AlertDish.setText(f"Preencha Todos Os Campos")
        else:
            New = Dish(-1, Name, Description, Price, Status)
            Id = Dish_DAO.AddDAO(New)
            New.Id = Id
            self.AddTableWidget(New)

    def DeleteDish(self):
        Line = self.Table.currentRow()

        LineId = self.Table.item(Line, 0)
        Id = LineId.text()
        self.Table.removeRow(Line)

        Dish_DAO.DeleteDAO(int(Id))

    def EditExpenses(self):
        Line = self.Table.currentRow()
        LineId = self.Table.item(Line, 0)
        Id = LineId.text()

        Name = self.InputName.text()
        Description = self.InputDescription.text()
        Price = self.InputPrice.text()
        Status = self.InputStatus.currentText()

        if Name == "" or Description == "" or Price == "" or Status == "":
            self.AlertErro.setText(f"Preencha Todos Os Campos")
        else:
            Update = Dish(-1, Name, Description, Price, Status)
            self.Edition(Update)
            Dish_DAO.EditDAO(Update, int(Id))

    def Edition(self, w: Dish):
        Line = self.Table.currentRow()

        Name = self.InputName.text()
        Description = self.InputDescription.text()
        Price = self.InputPrice.text()
        Status = self.InputStatus.currentText()

        Name = QTableWidgetItem(w.Name)
        Description = QTableWidgetItem(w.Description)
        Price = QTableWidgetItem(f"R$ {w.Price}")
        Status = QTableWidgetItem(w.Status)

        self.Table.setItem(Line, 1, Name)
        self.Table.setItem(Line, 2, Description)
        self.Table.setItem(Line, 3, Price)
        self.Table.setItem(Line, 4, Status)

    def GetText(self):
        Line = self.Table.currentRow()

        self.InputName.setText(self.Table.item(Line, 1).text())
        self.InputDescription.setText(self.Table.item(Line, 2).text())

    def AddTableWidget(self, w: Dish):
        Line = self.Table.rowCount()
        self.Table.insertRow(Line)

        Id = QTableWidgetItem(str(w.Id))
        Name = QTableWidgetItem(w.Name)
        Description = QTableWidgetItem(w.Description)
        Price = QTableWidgetItem(f"R$ {w.Price}")
        Status = QTableWidgetItem(w.Status)

        self.Table.setItem(Line, 0, Id)
        self.Table.setItem(Line, 1, Name)
        self.Table.setItem(Line, 2, Description)
        self.Table.setItem(Line, 3, Price)
        self.Table.setItem(Line, 4, Status)
