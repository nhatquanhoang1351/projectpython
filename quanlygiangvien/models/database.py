import sqlite3

class Database:
    def __init__(self, db_path='quanlygiangvien.db'):
        self.db_path = db_path
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
# import mysql.connector

# class Database:
#     def __init__(self, host='localhost', user='root', password='', database='quanlygiangvien'):
#         self.host = host
#         self.user = user
#         self.password = password
#         self.database = database
#         self.connection = None
#         self.cursor = None

#     def connect(self):
#         self.connection = mysql.connector.connect(
#             host=self.host,
#             user=self.user,
#             password=self.password,
#             database=self.database
#         )
#         self.cursor = self.connection.cursor(dictionary=True)
    def close(self):
        if self.connection:
            self.connection.close()

    def execute(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_all(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        return self.cursor.fetchone()