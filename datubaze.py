import sqlite3

db = sqlite3.connect('test.db')

db.execute("""CREATE TABLE IF NOT EXISTS dati
    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,vards 
    CHAR(50) NOT NULL
    )""")

def saglabat(vards):
   db.execute("""INSERT INTO dati
          (vards)
          VALUES (:vards)
          """,{'vards':vards})
db.commit()
