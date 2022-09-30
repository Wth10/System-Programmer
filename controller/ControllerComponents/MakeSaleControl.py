from PyQt6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem, QMessageBox
from PyQt6 import uic

File_Qt = "view/components/Sell.ui"

from model.Sales.Sales import Sales, GetDish
from model.Sales.Sales_DAO import Sales_DAO

from datetime import datetime
from datetime import date
import pandas as PD
import sqlite3


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

        self.BtnGetDish.clicked.connect(self.GetTextDish)
        self.BtnGetMakeSale.clicked.connect(self.GetTextMakeSale)
        self.BtnClean.clicked.connect(self.ClearField)
        self.GenerateExcel.clicked.connect(self.Excel)

        self.BtnAdd.clicked.connect(self.RegisterMakeSale)
        self.BtnEdit.clicked.connect(self.EditMakeSale)
        self.BtnDelete.clicked.connect(self.DeleteMakeSale)

        self.LoadTableDish()
        self.LoadTableMakeSale()

    def ClearField(self):
        self.InputName.clear()
        self.InputPrice.clear()
        self.InputObservation.clear()

    def GetTextDish(self):
        LineDish = self.DishTable.currentRow()

        if LineDish == -1:
            Alert = QMessageBox()
            Alert.setIcon(QMessageBox.Icon.Warning)
            Alert.setWindowTitle("Alerta")
            Alert.setText(
                "SELECIONE UMA LINHA NA TABELA DO CARDÁPIO PARA PEGAR OS DADOS!!"
            )
            Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            x = Alert.exec()
        else:
            self.InputName.setText(self.DishTable.item(LineDish, 1).text())
            self.InputPrice.setText(self.DishTable.item(LineDish, 2).text())

    def GetTextMakeSale(self):
        LineSale = self.SalesTable.currentRow()

        if LineSale == -1:
            Alert = QMessageBox()
            Alert.setIcon(QMessageBox.Icon.Warning)
            Alert.setWindowTitle("Alerta")
            Alert.setText(
                "SELECIONE UMA LINHA NA TABELA DE VENDAS PARA PEGAR OS DADOS!!"
            )
            Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            x = Alert.exec()
        else:
            self.InputName.setText(self.SalesTable.item(LineSale, 1).text())
            self.InputPrice.setText(self.SalesTable.item(LineSale, 2).text())
            self.InputObservation.setText(self.SalesTable.item(LineSale, 3).text())

    def Excel(self):
        connect = sqlite3.connect("./database/Restaurant.db")
        W = PD.read_sql_query("SELECT * FROM MakeSale", connect)
        W.to_excel("./DocsExcel/Lista_Vendas.xls", sheet_name="Vendas", index=False)

        Alert = QMessageBox()
        Alert.setIcon(QMessageBox.Icon.Information)
        Alert.setWindowTitle("Alerta")
        Alert.setText("PLANILHA CRIADA COM SUCESSO, ESTA NA PASTA 'DocsExcel' !!")
        Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
        x = Alert.exec()

    def RegisterMakeSale(self):
        Hour = datetime.now()

        Name = self.InputName.text()
        Price = self.InputPrice.text()
        Observation = self.InputObservation.text()
        PaymentMethod = self.InputPaymentMethod.currentText()
        Created_at = f"{date.today()}  {Hour.hour}:{Hour.minute}"

        if Name == "" or Price == "" or Observation == "" or PaymentMethod == "":
            Alert = QMessageBox()
            Alert.setIcon(QMessageBox.Icon.Warning)
            Alert.setWindowTitle("Alerta")
            Alert.setText("PREENCHA TODOS OS CAMPOS !!")
            Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            x = Alert.exec()
        else:
            New = Sales(-1, Name, Price, Observation, PaymentMethod, Created_at)
            Id = Sales_DAO.AddDAO(New)
            New.Id = Id
            self.AddTableMakeSale(New)

            Alert = QMessageBox()
            Alert.setIcon(QMessageBox.Icon.Information)
            Alert.setWindowTitle("Alerta")
            Alert.setText("VENDA REALIZADO COM SUCESSO!!")
            Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            x = Alert.exec()

            self.ClearField()

    def EditMakeSale(self):
        Line = self.SalesTable.currentRow()

        if Line == -1:
            Alert = QMessageBox()
            Alert.setIcon(QMessageBox.Icon.Warning)
            Alert.setWindowTitle("Alerta")
            Alert.setText("SELECIONE UMA LINHA NA TABELA DE VENDAS PARA EDITAR !!")
            Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            x = Alert.exec()
        else:
            Name = self.InputName.text()
            Price = self.InputPrice.text()
            Observation = self.InputObservation.text()
            PaymentMethod = self.InputPaymentMethod.currentText()

            if Name == "" or Price == "" or Observation == "" or PaymentMethod == "":
                Alert = QMessageBox()
                Alert.setIcon(QMessageBox.Icon.Information)
                Alert.setWindowTitle("Alerta")
                Alert.setText("PREENCHA TODOS OS CAMPOS !!")
                Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
                x = Alert.exec()
            else:
                LineId = self.SalesTable.item(Line, 0)
                Id = LineId.text()
                Update = Sales(-1, Name, Price, Observation, PaymentMethod, -1)
                self.Edition(Update)
                Sales_DAO.EditDAO(Update, int(Id))

                Alert = QMessageBox()
                Alert.setIcon(QMessageBox.Icon.Information)
                Alert.setWindowTitle("Alerta")
                Alert.setText("DADOS ATUALIZADOS COM REALIZADO COM SUCESSO!!")
                Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
                x = Alert.exec()

                self.ClearField()

    def Edition(self, w: Sales):
        Line = self.SalesTable.currentRow()

        Name = self.InputName.text()
        Price = self.InputPrice.text()
        Observation = self.InputObservation.text()
        PaymentMethod = self.InputPaymentMethod.currentText()

        Name = QTableWidgetItem(w.Name)
        Price = QTableWidgetItem(w.Price)
        Observation = QTableWidgetItem(w.Observation)
        PaymentMethod = QTableWidgetItem(w.Payment_Method)

        self.SalesTable.setItem(Line, 1, Name)
        self.SalesTable.setItem(Line, 2, Price)
        self.SalesTable.setItem(Line, 3, Observation)
        self.SalesTable.setItem(Line, 4, PaymentMethod)

    def DeleteMakeSale(self):
        Line = self.SalesTable.currentRow()

        if Line == -1:
            Alert = QMessageBox()
            Alert.setIcon(QMessageBox.Icon.Warning)
            Alert.setWindowTitle("Alerta")
            Alert.setText("SELECIONE UMA LINHA DA TABELA DE VENDAS !!")
            Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            x = Alert.exec()
        else:
            LineId = self.SalesTable.item(Line, 0)
            Id = LineId.text()

            Alert = QMessageBox()
            Alert.setIcon(QMessageBox.Icon.Warning)
            Alert.setWindowTitle("Alerta")
            Alert.setText(
                f"TEM CERTEZA QUE QUER APAGAR ESSA VENDA DO CARDÁPIO? CUJO Id {Id}"
            )
            Alert.setStandardButtons(
                QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
            )
            x = Alert.exec()

            if x == 1024:
                Line = self.SalesTable.currentRow()
                LineId = self.SalesTable.item(Line, 0)
                Id = LineId.text()
                self.SalesTable.removeRow(Line)
                Sales_DAO.DeleteDAO(int(Id))
            if x == 4194304:
                x = Alert.close()

    def LoadTableMakeSale(self):
        MakeSale_List = Sales_DAO.SelecMakeSale()
        for x in MakeSale_List:
            self.AddTableMakeSale(x)

    def AddTableMakeSale(self, w: Sales):
        Line = self.SalesTable.rowCount()
        self.SalesTable.insertRow(Line)

        Id = QTableWidgetItem(str(w.Id))
        Name = QTableWidgetItem(w.Name)
        Price = QTableWidgetItem(w.Price)
        Observation = QTableWidgetItem(w.Observation)
        Payment_Method = QTableWidgetItem(w.Payment_Method)
        Created_at = QTableWidgetItem(w.Created_at)

        self.SalesTable.setItem(Line, 0, Id)
        self.SalesTable.setItem(Line, 1, Name)
        self.SalesTable.setItem(Line, 2, Price)
        self.SalesTable.setItem(Line, 3, Observation)
        self.SalesTable.setItem(Line, 4, Payment_Method)
        self.SalesTable.setItem(Line, 5, Created_at)

    def LoadTableDish(self):
        self.DishTable.setRowCount(0)
        list_dish = Sales_DAO.SelectDish()
        for x in list_dish:
            self.AddTableDish(x)

    def AddTableDish(self, w: GetDish):
        Line = self.DishTable.rowCount()
        self.DishTable.insertRow(Line)

        Id = QTableWidgetItem(str(w.Id))
        Name = QTableWidgetItem(w.Name)
        Price = QTableWidgetItem(f"R$ {w.Price}")

        self.DishTable.setItem(Line, 0, Id)
        self.DishTable.setItem(Line, 1, Name)
        self.DishTable.setItem(Line, 2, Price)
