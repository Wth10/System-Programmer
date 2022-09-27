from .Dish import Dish
from database.Connect import ConnectDB as DB


class Dish_DAO:
    def AddDAO(w: Dish):
        connect = DB()
        cursor = connect.cursor()

        SQL = "INSERT INTO Dish(Name, Description, Price, Status, Created_at) VALUES (?, ?, ?, ?, ?);"
        Dados = [w.Name, w.Description, w.Price, w.Status, w.Created_at]
        cursor.execute(SQL, Dados)
        return_Id = cursor.execute("SELECT last_insert_rowid();")
        Id = return_Id.fetchall()[0][0]

        connect.commit()
        connect.close()

        return Id

    def EditDAO(w: Dish, Id: int):
        connect = DB()
        cursor = connect.cursor()

        SQL = "UPDATE Dish SET Name=?, Description=?, Price=?, Status=?, Created_at=? WHERE Id=?"
        Dados = [w.Name, w.Description, w.Price, w.Status, w.Created_at, Id]

        cursor.execute(SQL, Dados)
        connect.commit()
        connect.close()

    def DeleteDAO(Id: int):
        connect = DB()
        cursor = connect.cursor()

        SQL = "DELETE FROM Dish WHERE Id = ?;"
        cursor.execute(SQL, [Id])

        connect.commit()
        connect.close()

    def SelectAll() -> list:
        Dish_List = []

        connect = DB()
        cursor = connect.cursor()
        SQL = "SELECT * FROM Dish ORDER BY Status ASC;"
        cursor.execute(SQL)

        list = cursor.fetchall()
        for x in list:
            w = Dish(x[0], x[1], x[2], x[3], x[4], x[5])
            Dish_List.append(w)
        connect.close()

        return Dish_List
