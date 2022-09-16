import sqlite3


File = "./database/Restaurant.db"


def ConnectDB():
    w = sqlite3.connect(File)
    return w
