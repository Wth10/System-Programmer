from PyQt6.QtWidgets import QWidget, QHeaderView
from PyQt6 import uic

File_Qt = "view/components/Employees.ui"


class EmployeeControl(QWidget):
    def __init__(self) -> None:
        super(EmployeeControl, self).__init__()
        uic.loadUi(File_Qt, self)

        self.Table.horizontalHeader().setStretchLastSection(True)
        self.Table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
