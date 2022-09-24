from PyQt6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem, QMessageBox
from PyQt6 import uic

from model.Employees.Employees import Employees
from model.Employees.Employees_DAO import Employees_DAO

from datetime import datetime
from datetime import date

File_Qt = "view/components/Employees.ui"


class EmployeeControl(QWidget):
    def __init__(self) -> None:
        super(EmployeeControl, self).__init__()
        uic.loadUi(File_Qt, self)

        self.Table.horizontalHeader().setStretchLastSection(True)
        self.Table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.LoadData()

        self.BtnAdd.clicked.connect(self.RegisterEmployees)
        self.BtnEdit.clicked.connect(self.EditEmployees)
        self.BtnDelete.clicked.connect(self.DeleteEmployees)

        self.BtnGetData.clicked.connect(self.GetText)
        self.BtnClean.clicked.connect(self.ClearField)

    def LoadData(self):
        list = Employees_DAO.SelectAll()
        for x in list:
            self.AddTableWidget(x)

    def ClearField(self):
        self.InputName.clear()
        self.InputOccupation.clear()
        self.Alert.clear()

    def GetText(self):
        Line = self.Table.currentRow()

        if Line == -1:
            Alert = QMessageBox()
            Alert.setIcon(QMessageBox.Icon.Information)
            Alert.setWindowTitle("Alerta")
            Alert.setText("SELECIONE UMA LINHA NA TABELA PARA PEGAR OS DADOS !!")
            Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            x = Alert.exec()
        else:
            self.InputName.setText(self.Table.item(Line, 1).text())
            self.InputOccupation.setText(self.Table.item(Line, 2).text())

    def RegisterEmployees(self):
        Hour = datetime.now()

        Name = self.InputName.text()
        Occupation = self.InputOccupation.text()
        Remuneration = self.InputRemuneration.text()
        Status = self.InputStatus.currentText()
        DateTime = f"{date.today()}  {Hour.hour}:{Hour.minute}"

        if Name == "" or Occupation == "" or Remuneration == "" or Status == "":
            self.Alert.setText(f"Preencha Todos Os Campos")
        else:
            New = Employees(-1, Name, Occupation, Remuneration, Status, DateTime)
            Id = Employees_DAO.AddDAO(New)
            New.Id = Id
            self.AddTableWidget(New)

            Alert = QMessageBox()
            Alert.setIcon(QMessageBox.Icon.Information)
            Alert.setWindowTitle("Alerta")
            Alert.setText("CADASTRO REALIZADO COM SUCESSO!!")
            Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            x = Alert.exec()

            self.ClearField()

    def DeleteEmployees(self):
        Line = self.Table.currentRow()

        if Line == -1:
            Alert = QMessageBox()
            Alert.setIcon(QMessageBox.Icon.Warning)
            Alert.setWindowTitle("Alerta")
            Alert.setText("SELECIONE UMA LINHA NA TABELA!!")
            Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            x = Alert.exec()
        else:
            LineId = self.Table.item(Line, 0)
            Id = LineId.text()

            Alert = QMessageBox()
            Alert.setIcon(QMessageBox.Icon.Warning)
            Alert.setWindowTitle("Alerta")
            Alert.setText(f"TEM CERTEZA QUE QUER APAGAR ESSE FUNCIONÁRIO? CUJO Id {Id}")
            Alert.setStandardButtons(
                QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
            )
            x = Alert.exec()

            if x == 1024:
                Line = self.Table.currentRow()
                LineId = self.Table.item(Line, 0)
                Id = LineId.text()
                self.Table.removeRow(Line)
                Employees_DAO.DeleteDAO(int(Id))
            if x == 4194304:
                x = Alert.close()

    def EditEmployees(self):
        Hour = datetime.now()

        Line = self.Table.currentRow()

        if Line == -1:
            Alert = QMessageBox()
            Alert.setIcon(QMessageBox.Icon.Warning)
            Alert.setWindowTitle("Alerta")
            Alert.setText("SELECIONE UMA LINHA NA TABELA!!")
            Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            x = Alert.exec()
        else:
            Name = self.InputName.text()
            Occupation = self.InputOccupation.text()
            Remuneration = self.InputRemuneration.text()
            Status = self.InputStatus.currentText()
            DateTime = f"{date.today()}  {Hour.hour}:{Hour.minute}"

            if Name == "" or Occupation == "" or Remuneration == "" or Status == "":
                self.Alert.setText(f"Preencha Todos Os Campos")
            else:
                LineId = self.Table.item(Line, 0)
                Id = LineId.text()
                Update = Employees(-1, Name, Occupation, Remuneration, Status, DateTime)
                self.Edition(Update)
                Employees_DAO.EditDAO(Update, int(Id))

                Alert = QMessageBox()
                Alert.setIcon(QMessageBox.Icon.Information)
                Alert.setWindowTitle("Alerta")
                Alert.setText("DADOS ATUALIZADOS COM REALIZADO COM SUCESSO!!")
                Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
                x = Alert.exec()

                self.ClearField()

    def Edition(self, w: Employees):
        Line = self.Table.currentRow()

        Name = self.InputName.text()
        Occupation = self.InputOccupation.text()
        Remuneration = self.InputRemuneration.text()
        Status = self.InputStatus.currentText()

        Name = QTableWidgetItem(w.Name)
        Occupation = QTableWidgetItem(w.Occupation)
        Remuneration = QTableWidgetItem(f"R$ {w.Remuneration}")
        Status = QTableWidgetItem(w.Status)

        self.Table.setItem(Line, 1, Name)
        self.Table.setItem(Line, 2, Occupation)
        self.Table.setItem(Line, 3, Remuneration)
        self.Table.setItem(Line, 4, Status)

    def AddTableWidget(self, w: Employees):
        Line = self.Table.rowCount()
        self.Table.insertRow(Line)

        Id = QTableWidgetItem(str(w.Id))
        Name = QTableWidgetItem(w.Name)
        Occupation = QTableWidgetItem(w.Occupation)
        Remuneration = QTableWidgetItem(f"R$ {w.Remuneration}")
        Status = QTableWidgetItem(w.Status)
        Created_at = QTableWidgetItem(w.Created_at)

        self.Table.setItem(Line, 0, Id)
        self.Table.setItem(Line, 1, Name)
        self.Table.setItem(Line, 2, Occupation)
        self.Table.setItem(Line, 3, Remuneration)
        self.Table.setItem(Line, 4, Status)
        self.Table.setItem(Line, 5, Created_at)
