from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

from controller.ControllerComponents.Menu import Menu
from controller.ControllerComponents.Employees import Employees
from controller.ControllerComponents.Profile import Profile
from controller.ControllerComponents.Dish import Dish

File_Qt = "view/Dashboard.ui"


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        uic.loadUi(File_Qt, self)

        self.setWindowTitle("ESPETO DE BOI")
        self.showMaximized()

        # Cria os objetos das páginas
        self.PageMenu = Menu()
        self.PageEmployees = Employees()
        self.PageProfile = Profile()
        self.PageDish = Dish()

        # Insere as páginas
        self.StackedWidget.addWidget(self.PageMenu)
        self.StackedWidget.addWidget(self.PageEmployees)
        self.StackedWidget.addWidget(self.PageProfile)
        self.StackedWidget.addWidget(self.PageDish)

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
