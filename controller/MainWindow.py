from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

from controller.ControllerLayout.Login import Login
from controller.ControllerLayout.Registration import Cadastro

File_Qt = "view/Home.ui"


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        uic.loadUi(File_Qt, self)

        self.setWindowTitle("ESPETO DE BOI")
        self.showMaximized()

        # Cria os objetos das páginas
        self.PagLogin = Login()
        self.PagCadastro = Cadastro()

        # Insere as páginas
        self.StackedWidget.addWidget(self.PagLogin)
        self.StackedWidget.addWidget(self.PagCadastro)

        # Ações dos botões
        self.BtnLogin.clicked.connect(self.ActionMenu)
        self.BtnCadastro.clicked.connect(self.ActionMenu)

    def ActionMenu(self):
        Button = self.sender()
        ClickedButton = Button.objectName()

        if ClickedButton == "BtnLogin":
            self.StackedWidget.setCurrentIndex(0)

        if ClickedButton == "BtnCadastro":
            self.StackedWidget.setCurrentIndex(1)
