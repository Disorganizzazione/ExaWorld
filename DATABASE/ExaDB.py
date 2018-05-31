from DBInterface import *
import psycopg2


class ExaDB(DBInterface):
    def __init__(self):
        super().__init__()
    def getConnect(self):     
        conn="dbname='exaworld' user='postgres' host='localhost' "
        try:
            db=psycopg2.connect(conn)
        except:
            print("dbconnection fail")
        else:
            print("tutto bene")
            return db.cursor()

    def getTerrain(self ,code):
        cur = self.getConnect()
        cur.execute("select * from World.terreno as x where x.codice= %s ;" ,(code, ))
        return cur.fetchone()
    
    def searchCode(self, code, cur):
        b=None
        for a in cur:
            if (code!=a[0]):
                continue  
            else:
                b=a
                break
        if (b==None):
            return "fine"
        else:
            return b

    def getPlant(self,code):
        cur = self.getConnect()
        cur.execute("select * from World.piante as pi join World.comportamento as co on co.id=pi.comp;")
        return self.searchCode(code, cur)

    def getHerbivore(self, code):
        cur = self.getConnect()
        cur.execute("select * from World.erbivori as er join World.comportamento as co on co.id=er.comp;")
        return self.searchCode(code, cur)

    def getCarnivorous(self, code):
        cur = self.getConnect()
        cur.execute("select * from World.carnivori as ca join World.comportamento as co on co.id=ca.comp;")
        return self.searchCode(code, cur)

    def getOmnivorous(self, code):
        cur = self.getConnect()
        cur.execute("select * from World.onnivori as om join World.comportamento as co on co.id=om.comp;")
        return self.searchCode(code, cur)

db=ExaDB()

print(db.getPlant(5)) 
print(db.getHerbivore(2))
print(db.getOmnivorous(6))



