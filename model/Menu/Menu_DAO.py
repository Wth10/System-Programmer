from .Menu import Menu
from database.Connect import ConnectDB as DB


class Menu_DAO:
    def PlateCount():
        connect = DB()
        cursor = connect.cursor()

        SQL = "SELECT count(Id) FROM Dish WHERE Status = 'Ativo';"

        w = cursor.execute(SQL)
        x = w.fetchone()[0]
        connect.close()
        return x

    def getName():
        connect = DB()
        cursor = connect.cursor()
        SQL = "SELECT Name FROM Dish WHERE Status = 'Ativo';"
        cursor.execute(SQL)

        x = cursor.fetchall()

        connect = DB()
        cursor = connect.cursor()

        return x

    def getPrice():
        connect = DB()
        cursor = connect.cursor()
        SQL = "SELECT Price FROM Dish WHERE Status = 'Ativo';"
        cursor.execute(SQL)

        x = cursor.fetchall()

        connect = DB()
        cursor = connect.cursor()

        return x

    def getDescription():
        connect = DB()
        cursor = connect.cursor()
        SQL = "SELECT Description FROM Dish WHERE Status = 'Ativo';"
        cursor.execute(SQL)

        x = cursor.fetchall()

        connect = DB()
        cursor = connect.cursor()

        return x
