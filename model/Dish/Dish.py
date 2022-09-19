class Dish:
    def __init__(self, Id, Name, Description, Price, Status) -> None:
        self.Id = Id
        self.Name = Name
        self.Description = Description
        self.Price = Price
        self.Status = Status


class EditDish:
    def __init__(self, Name, Description, Price, Status) -> None:
        self.Name = Name
        self.Description = Description
        self.Price = Price
        self.Status = Status
