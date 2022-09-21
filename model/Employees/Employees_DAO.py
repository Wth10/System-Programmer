from .Employees import Employees
from database.Connect import ConnectDB as DB


class Employees_DAO:
    def AddDAO(w: Employees):
        connect = DB()
        cursor = connect.cursor()

        SQL = "INSERT INTO Employees(Name, Occupation, Remuneration, Status, Created_at) VALUES (?, ?, ?, ?, ?);"
        Dados = [w.Name, w.Occupation, w.Remuneration, w.Status, w.Created_at]
        cursor.execute(SQL, Dados)
        return_Id = cursor.execute("SELECT last_insert_rowid();")
        Id = return_Id.fetchall()[0][0]

        connect.commit()
        connect.close()

        return Id

    def EditDAO(w: Employees, Id: int):
        connect = DB()
        cursor = connect.cursor()

        SQL = "UPDATE Employees SET Name=?, Occupation=?, Remuneration=?, Status=? WHERE Id=?"
        Dados = [w.Name, w.Occupation, w.Remuneration, w.Status, Id]

        cursor.execute(SQL, Dados)
        connect.commit()
        connect.close()

    def DeleteDAO(Id: int):
        connect = DB()
        cursor = connect.cursor()

        SQL = "DELETE FROM Employees WHERE Id = ?;"
        cursor.execute(SQL, [Id])

        connect.commit()
        connect.close()

    def SelectAll() -> list:
        Employees_List = []

        connect = DB()
        cursor = connect.cursor()
        SQL = "SELECT * FROM Employees ORDER BY Status ASC;"
        cursor.execute(SQL)

        list = cursor.fetchall()
        for x in list:
            w = Employees(x[0], x[1], x[2], x[3], x[4], x[5])
            Employees_List.append(w)
        connect.close()

        return Employees_List
