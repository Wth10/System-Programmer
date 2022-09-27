from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

from controller.ControllerLayout.LoginControl import LoginControl
from controller.ControllerLayout.RegistrationControl import RegistrationControl


File_Qt = "view/Home.ui"


class MainLogin(QWidget):
    def __init__(self) -> None:
        super(MainLogin, self).__init__()
        uic.loadUi(File_Qt, self)

        self.setWindowTitle("ESPETO DE BOI")
        self.showMaximized()

        self.PageLogin = LoginControl()
        self.PageRegistration = RegistrationControl()

        self.StackedWidget.addWidget(self.PageLogin)
        self.StackedWidget.addWidget(self.PageRegistration)

        self.BtnLogin.clicked.connect(self.ActionMenu)
        self.BtnCadastro.clicked.connect(self.ActionMenu)

    def ActionMenu(self):
        Button = self.sender()
        ClickedButton = Button.objectName()

        if ClickedButton == "BtnLogin":
            self.StackedWidget.setCurrentIndex(0)

        if ClickedButton == "BtnCadastro":
            self.StackedWidget.setCurrentIndex(1)
