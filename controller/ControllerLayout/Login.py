from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

File_Qt = "view/layout/Login.ui"


class Login(QWidget):
    def __init__(self) -> None:
        super(Login, self).__init__()
        uic.loadUi(File_Qt, self)

        self.BtnLogin.clicked.connect(self.Login)

    def Login(self):
        Email = self.InputEmail.text()
        Password = self.InputPassword.text()

        if Email == "" or Password == "":
            self.AlertLogin.setText(f"Campos Em Branco")
        else:
            self.AlertLogin.setText(f"OK!")
