from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic


File_Qt = "view/layout/Cadastro.ui"


class RegistrationControl(QWidget):
    def __init__(self) -> None:
        super(RegistrationControl, self).__init__()
        uic.loadUi(File_Qt, self)

        self.BtnCadastro.clicked.connect(self.Registration)

    def Registration(self):
        Name = self.InputName.text()
        Email = self.InputEmail.text()
        Password = self.InputPassword.text()

        if Name == "" or Email == "" or Password == "":
            Alert = QMessageBox()
            Alert.setIcon(QMessageBox.Icon.Information)
            Alert.setWindowTitle("Alerta")
            Alert.setText("PREENCHA TODOS OS CAMPOS !!")
            Alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            x = Alert.exec()
        else:
            pass
