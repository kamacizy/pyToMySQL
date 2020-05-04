import mysql.connector as mysql

class MySQL:
    def __init__(self, hostname: str, user: str, password: str, db_name, table_name: str):
        self.db = mysql.connect(
            host = hostname,
            user = user,
            passwd = password,
            database = db_name
        )
        self.cursor = self.db.cursor()

        self.table_name = table_name
        self.db.get_

    def table(self):
        self.cursor.execute("CREATE TABLE "+str(table_name)+" (name VARCHAR(255), user_name VARCHAR(255))")