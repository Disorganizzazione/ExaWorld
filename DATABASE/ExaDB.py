from DBInterface import *
import psycopg2


class ExaDB(DBInterface):

    def __init__(self):
        super().__init__()
    def getConnect(self):     
        conn="dbname='exaworld' user='postgres' host='localhost' "
        try:
            db=psycopg2.connect(conn)
            return db.cursor()
        except:
            print("dbconnection fail")
            print("ok")
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
        cur.execute("select id, nome, resistenza, riprod, tmin, tmax, umin, umax from world.creature where tipo= 'v'")
        return self.searchCode(code, cur)

    def getAnimal(self, code):
        cur = self.getConnect()
        cur.execute("select cre.id, cre.nome, resistenza, forza, velocita, dieta, tmin, tmax, umin, umax, com.nome as compor, aggressività, branco, sedentarietà, riproduzione  from world.creature as cre join world.comportamento as com on cre.comp=com.id where tipo = 'a';")
        return self.searchCode(code, cur)

    def getcreature(self, code):
            cur = self.getConnect()
            cur.execute("select id,tipo from world.creature;")
            if self.searchCode(code, cur)[1] == "a":
                return self.getAnimal(code)
            else :
                return self.getPlant(code)
    
a=ExaDB()
a.getConnect()
for b in range(1,10):
    print(a.getcreature(b)[1])






