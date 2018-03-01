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
            return db.cousor()

    def getTerrain(self):
        with 
llonzo=dbInterface()
db=llonzo.getConnect()

