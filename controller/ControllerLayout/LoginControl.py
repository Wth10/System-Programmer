from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic

from ..MainWindow import MainWindow

File_Qt = "view/layout/Login.ui"


class LoginControl(QWidget):
    def __init__(self) -> None:
        super(LoginControl, self).__init__()
        uic.loadUi(File_Qt, self)

        self.BtnLogin.clicked.connect(self.Login)

    def Login(self):
        Email = self.InputEmail.text()
        Password = self.InputPassword.text()

        if Email == "" or Password == "":
            Alert = QMessageBox()
            Alert.setIcon(QMessageBox.Icon.Information)
            Alert.setWindowTitle("Alerta")
            Alert.setText("PREENCHA TODOS OS CAMPOS !!")
            Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            x = Alert.exec()
        else:
            if Email == "1" and Password == "1":
                self.hide()
                W = MainWindow()
                W.show()
            else:
                Alert = QMessageBox()
                Alert.setIcon(QMessageBox.Icon.Information)
                Alert.setWindowTitle("Alerta")
                Alert.setText("DADOS INCORRETOS !!")
                Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
                x = Alert.exec()
