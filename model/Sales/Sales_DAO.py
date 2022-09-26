from .Sales import Sales
from database.Connect import ConnectDB as DB


class Sales_DAO:
    def SelectDish() -> list:
        Dish_List = []

        connect = DB()
        cursor = connect.cursor()
        SQL = "SELECT Id, Name, Price FROM Dish WHERE Status == 'Ativo'"
        cursor.execute(SQL)

        list = cursor.fetchall()
        for x in list:
            w = Sales(x[0], x[1], x[2])
            Dish_List.append(w)
        connect.close()

        return Dish_List
