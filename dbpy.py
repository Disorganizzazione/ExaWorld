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
    
    def getPlant(self,code):
        cur = self.getConnect()
        cur.execute("select * from World.piante join World.comportamento on World.comportamento.id=World.piante.comp;")
        for a in cur:
            if ( a == None):
                return "fine"
        return a    

db=dbInterface()
print(db.getPlant(3))




