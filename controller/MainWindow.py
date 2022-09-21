from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

from controller.ControllerComponents.MenuControl import MenuControl
from controller.ControllerComponents.EmployeeControl import EmployeeControl
from controller.ControllerComponents.ProfileControl import ProfileControl
from controller.ControllerComponents.PlateControl import PlateControl

File_Qt = "view/Dashboard.ui"


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        uic.loadUi(File_Qt, self)

        self.setWindowTitle("ESPETO DE BOI")
        self.showMaximized()

        # Cria os objetos das páginas
        self.PageMenuControl = MenuControl()
        self.PageEmployeeControl = EmployeeControl()
        self.PageProfileControl = ProfileControl()
        self.PagePlateControl = PlateControl()

        # Insere as páginas
        self.StackedWidget.addWidget(self.PageMenuControl)
        self.StackedWidget.addWidget(self.PageEmployeeControl)
        self.StackedWidget.addWidget(self.PageProfileControl)
        self.StackedWidget.addWidget(self.PagePlateControl)

        # Ações dos botões
        self.BtnMenu.clicked.connect(self.ActionMenu)
        self.BtnEmployees.clicked.connect(self.ActionMenu)
        self.BtnProfile.clicked.connect(self.ActionMenu)
        self.BtnDish.clicked.connect(self.ActionMenu)

    def ActionMenu(self):
        Button = self.sender()
        ClickedButton = Button.objectName()

        if ClickedButton == "BtnMenu":
            self.StackedWidget.setCurrentIndex(0)

        if ClickedButton == "BtnEmployees":
            self.StackedWidget.setCurrentIndex(1)

        if ClickedButton == "BtnProfile":
            self.StackedWidget.setCurrentIndex(2)

        if ClickedButton == "BtnDish":
            self.StackedWidget.setCurrentIndex(3)
