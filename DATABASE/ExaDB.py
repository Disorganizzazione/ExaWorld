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
        cur.execute("select * from World.piante;")
        return self.searchCode(code, cur)

    def getAnimal(self, code):
        cur = self.getConnect()
        cur.execute("select * from World.animali as an join World.comportamento as co on co.id=an.comp;")
        return self.searchCode(code, cur)
    
a=ExaDB()
a.getConnect()
for b in range(1,6):
    print(a.getAnimal(b))
    print(a.getPlant(b))
    print(b)





