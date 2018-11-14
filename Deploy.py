from DATABASE import DBclass
import random
from CONCEPT import Snippet

class content():

    def __init__(self):
        self.content={}

    def creation(self, gxel, xel, temp, umid):
        print(str(temp),"  ", str(umid))

        if gxel not in self.content.keys() :
            self.content[gxel]={}
        
        if xel not in self.content[gxel].keys():
            animal=[]
            vegetal=[]
            terrain=[]
            db=DBclass.ExaDB()
            a=1
            for i in db.creatures:
                creatures= DBclass.Creature(db,a)
                if creatures.tipo== "vegetale":
                    if temp <= creatures.maxtemp and temp >= creatures.mintemp  and umid <= creatures.maxhmd and umid >= creatures.minhmd:
                        vegetal.append(creatures)
                    vegetal.append(None)
                else:
                    if temp <= creatures.maxtemp and temp >= creatures.mintemp  and umid <= creatures.maxhmd and umid >= creatures.minhmd:
                        animal.append(creatures)
                    animal.append(None)
                a=a+1

            
            
            a=1
            for i in db.terrains:
                terr= DBclass.Terrain(db,a)
                if temp <= terr.maxtemp and temp >= terr.mintemp  and umid <= terr.maxhmd and umid >= terr.minhmd:
                    terrain.append(terr)
                terrain.append(None)
                a=a+1

            


            indexa=random.randint(0,len(animal)-1)
            indexv=random.randint(0,len(vegetal)-1)
            indext=random.randint(0,len(terrain)-1)

            self.content[gxel][xel]=(animal[indexa],vegetal[indexv],terrain[indext])

            return self.content[gxel][xel]

        else:
            return self.content[gxel][xel]

    def filedictionary(self, gxel):
        if gxel not in self.content.keys() :
            self.content[gxel]=Snippet.load(gxel)
            if self.content[gxel]== -1 :
                return "errore mappa non creata"
            

    def dictionaryfile(self, gxel):
        Snippet.save(self.content[gxel])
        self.content.pop(gxel)

    def getcontent (gxel, xel):
        return self.content[gxel][xel]



#con=content()
#print(con.creation((0,0),(32,45,8),23,20))


