import sqlite3
import hashlib

class DataBase:
    connection = None
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        cursor = self.connection.cursor()
        create_table_query = '''CREATE TABLE IF NOT EXISTS User_types (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                utype TEXT NOT NULL UNIQUE);'''
        cursor.execute(create_table_query)
        self.connection.commit()
        create_table_query = '''CREATE TABLE IF NOT EXISTS Users (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    login TEXT NOT NULL UNIQUE,
                                    password TEXT NOT NULL UNIQUE,
                                    utype_id INTEGER,
                                    FOREIGN KEY (utype_id) REFERENCES User_types(id) 
                                    ON DELETE CASCADE);'''

        cursor.execute(create_table_query)
        self.connection.commit()
        cursor.execute('SELECT count(*) FROM Users WHERE utype_id = 1')
        admins_count = cursor.fetchall()[0][0]
        if admins_count == 0:
            insert_query = "INSERT INTO Users (login, password, utype_id) VALUES (?,?,?);"
            hashed = hashlib.md5('admin'.encode('utf-8')).hexdigest()
            cursor.execute(insert_query, ('admin', hashed, 1))
            self.connection.commit()
        cursor.close()
    def cursor(self):
        return self.connection.cursor()
    def commit(self):
        self.connection.commit()
    def __del__(self):
        self.connection.close()
