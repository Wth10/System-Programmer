class Employees:
    def __init__(self, Id, Name, Occupation, Remuneration, Status, Created_at) -> None:
        self.Id = Id
        self.Name = Name
        self.Occupation = Occupation
        self.Remuneration = Remuneration
        self.Status = Status
        self.Created_at = Created_at


class EditEmployees:
    def __init__(self, Name, Occupation, Remuneration, Status) -> None:
        self.Name = Name
        self.Occupation = Occupation
        self.Remuneration = Remuneration
        self.Status = Status
