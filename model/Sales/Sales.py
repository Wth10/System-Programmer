class Sales:
    def __init__(
        self, Id, Name, Price, Observation, Payment_Method, Created_at
    ) -> None:
        self.Id = Id
        self.Name = Name
        self.Price = Price
        self.Observation = Observation
        self.Payment_Method = Payment_Method
        self.Created_at = Created_at


class GetDish:
    def __init__(self, Id, Name, Price) -> None:
        self.Id = Id
        self.Name = Name
        self.Price = Price
