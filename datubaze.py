import sqlite3

db = sqlite3.connect('test.db', check_same_thread = False)

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

def datu_atgriesana():
  dati = db.execute("SELECT * FROM dati")


  rezultats = dati.fetchall()

  for rinda in rezultats:
   print("ID",rinda[0])
   print("vards:",rinda[1])
datu_atgriesana()