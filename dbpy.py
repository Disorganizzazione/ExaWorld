from dinterface import *
import psycopg2

class dbInterface(Datainterface):
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
        pass
    #NON SIAMO CAPACI A CHIAMARE UNA FUNZIONE DENTRO AD UN'ALTRA
    def getPlant(self,code):
        cur = self.getConnect()
        cur.execute("select * from World.piante join World.comportamento "+
        "on World.comportamento.id=World.piante.comp;")
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
    
    def getHerbivore(self, code):
        cur = self.getConnect()
        cur.execute("select * from World.erbivori join World.comportamento "+
        "on World.comportamento.id=World.erbivori.comp;")
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

    def getCarnivorous(self, code):
        pass
    def getOmnivorous(self, code):
        pass

db=dbInterface()

print(db.getPlant(3))
    
print(db.getHerbivore(2))




