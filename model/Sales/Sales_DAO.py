from .Sales import Sales, GetDish
from database.Connect import ConnectDB as DB


class Sales_DAO:
    def AddDAO(w: Sales):
        connect = DB()
        cursor = connect.cursor()

        SQL = "INSERT INTO MakeSale(Name, Price, Observation, Payment_Method, Created_at) VALUES (?, ?, ?, ?, ?);"
        Dados = [w.Name, w.Price, w.Observation, w.Payment_Method, w.Created_at]
        cursor.execute(SQL, Dados)
        return_Id = cursor.execute("SELECT last_insert_rowid();")
        Id = return_Id.fetchall()[0][0]

        connect.commit()
        connect.close()

        return Id

    def EditDAO(w: Sales, Id: int):
        connect = DB()
        cursor = connect.cursor()

        SQL = "UPDATE MakeSale SET Name=?, Price=?, Observation=?, Payment_Method=? WHERE Id=?"
        Dados = [w.Name, w.Price, w.Observation, w.Payment_Method, Id]

        cursor.execute(SQL, Dados)
        connect.commit()
        connect.close()

    def DeleteDAO(Id: int):
        connect = DB()
        cursor = connect.cursor()

        SQL = "DELETE FROM MakeSale WHERE Id = ?;"
        cursor.execute(SQL, [Id])

        connect.commit()
        connect.close()

    def SelectDish() -> list:
        Dish_List = []

        connect = DB()
        cursor = connect.cursor()
        SQL = "SELECT Id, Name, Price FROM Dish WHERE Status == 'Ativo'"
        cursor.execute(SQL)

        list = cursor.fetchall()
        for x in list:
            w = GetDish(x[0], x[1], x[2])
            Dish_List.append(w)
        connect.close()

        return Dish_List

    def SelecMakeSale() -> list:
        MakeSale_List = []

        connect = DB()
        cursor = connect.cursor()
        SQL = "SELECT * FROM MakeSale"
        cursor.execute(SQL)

        list = cursor.fetchall()
        for x in list:
            w = Sales(x[0], x[1], x[2], x[3], x[4], x[5])
            MakeSale_List.append(w)
        connect.close()

        return MakeSale_List
