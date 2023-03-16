
import sqlite3


class Database:
    def __init__(self, name="") -> None:
        self.name = name
        
    def connect_db(self):
        return sqlite3.connect(str(self.name))

    def create_table(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE t(a,b);")
        conn.commit()
        conn.close()

db = Database("D://GIT_CODE//GLOBANT//globantTest//04 - database//globant.db")
db.create_table()
