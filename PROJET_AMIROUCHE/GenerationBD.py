import sqlite3

conn = sqlite3.connect('baseDonnees.db')
cur = conn.cursor()

datas = [
    (1,'Amirouche','Ammour','img'),
    (2,'Younes','Benzair','img'),
    (3,'Falilou','Diop','img'),
 ]

cur.execute("CREATE TABLE IF NOT EXISTS BASE(id INT, prenom TEXT, nom TXT, img TXT)")
cur.executemany("INSERT INTO BASE(id,prenom,nom,img) VALUES(?, ?, ?, ?)", datas)
conn.commit()

cur.close()
conn.close()
