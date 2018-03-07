from dinterface import *
import psycopg2

class dbInterface(Datainterface):
    def getConnect(self):     
        conn="dbname='exaworld' user='filippo' host='localhost' "
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
        cur.execute("select * from World.piante ;")
        b=None
        a=0
        for a in range(0,code):
            b=cur.fetchone()
            if ( b == None):
                return "fine"
        return b    

db=dbInterface()
print(db.getPlant(2))




