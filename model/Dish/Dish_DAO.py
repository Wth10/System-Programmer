from .Dish import Dish
from database.Connect import ConnectDB as DB


class Dish_DAO:
    def AddDAO(w: Dish):
        connect = DB()
        cursor = connect.cursor()

        SQL = "INSERT INTO Dish(Name, Description, Price, Status) VALUES (?,?,?,?);"
        Dados = [w.Name, w.Description, w.Price, w.Status]
        cursor.execute(SQL, Dados)
        return_Id = cursor.execute("SELECT last_insert_rowid();")
        Id = return_Id.fetchall()[0][0]

        connect.commit()
        connect.close()

        return Id

    def SelectAll() -> list:
        Dish_List = []

        connect = DB()
        cursor = connect.cursor()
        SQL = "SELECT * FROM Dish;"
        cursor.execute(SQL)

        list = cursor.fetchall()
        for x in list:
            w = Dish(x[0], x[1], x[2], x[3], x[4])
            Dish_List.append(w)
        connect.close()

        return Dish_List
