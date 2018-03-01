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

    def getTerrain(self,code):
        cur = self.getConnect()

        return cur.execute("select * from terreno where codice=%s ", (code))
llonzo=dbInterface()
db=llonzo.getTerrain(2)
print("db");

