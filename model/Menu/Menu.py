class Menu:
    def __init__(self, Name, Description, Price) -> None:
        self.Name = Name
        self.Description = Description
        self.Price = Price

    def getName(self):
        return self.Name
