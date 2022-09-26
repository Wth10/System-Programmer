from PyQt6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem, QMessageBox
from PyQt6 import uic

File_Qt = "view/components/Sell.ui"

from model.Sales.Sales import Sales
from model.Sales.Sales_DAO import Sales_DAO


class MakeSaleControl(QWidget):
    def __init__(self) -> None:
        super(MakeSaleControl, self).__init__()
        uic.loadUi(File_Qt, self)

        self.DishTable.horizontalHeader().setStretchLastSection(True)
        self.DishTable.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.SalesTable.horizontalHeader().setStretchLastSection(True)
        self.SalesTable.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.BtnGetData.clicked.connect(self.GetText)
        self.BtnClean.clicked.connect(self.ClearField)

        self.LoadData()

    def ClearField(self):
        self.InputName.clear()
        self.InputPrice.clear()
        self.InputDescription.clear()

    def GetText(self):
        Line = self.DishTable.currentRow()

        if Line == -1:
            Alert = QMessageBox()
            Alert.setIcon(QMessageBox.Icon.Warning)
            Alert.setWindowTitle("Alerta")
            Alert.setText("SELECIONE UMA LINHA NA TABELA PARA PEGAR OS DADOS!!")
            Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            x = Alert.exec()
        else:
            self.InputName.setText(self.DishTable.item(Line, 1).text())
            self.InputPrice.setText(self.DishTable.item(Line, 2).text())

    def LoadData(self):
        list_dish = Sales_DAO.SelectDish()
        for x in list_dish:
            self.AddTableDish(x)

    def AddTableDish(self, w: Sales):
        Line = self.DishTable.rowCount()
        self.DishTable.insertRow(Line)

        Id = QTableWidgetItem(str(w.Id))
        Name = QTableWidgetItem(w.Name)
        Price = QTableWidgetItem(f"R$ {w.Price}")

        self.DishTable.setItem(Line, 0, Id)
        self.DishTable.setItem(Line, 1, Name)
        self.DishTable.setItem(Line, 2, Price)
