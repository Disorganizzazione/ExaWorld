import sys
sys.path.append("../")
import DATABASE.DBclass
import random
from CONCEPT import Snippet

class content():

    def __init__(self):
        self.content={}

    def creation(self, gxel, xel, temp, umid):
        animal=[]
        vegetal=[]
        terrain=[]
        db=DATABASE.DBclass.ExaDB()
        a=1
        for i in db.creatures:
            creatures=DATABASE.DBclass.Creature(db,a)
            if creatures.tipo== "vegetale":
                if temp <= creatures.maxtemp and temp >= creatures.mintemp  and umid <= creatures.maxhmd and umid >= creatures.minhmd:
                    vegetal.append(creatures)
            else:
                if temp <= creatures.maxtemp and temp >= creatures.mintemp  and umid <= creatures.maxhmd and umid >= creatures.minhmd:
                    animal.append(creatures)
            a=a+1

        animal.append(None)
        vegetal.append(None)
        a=1
        for i in db.terrains:
            terr=DATABASE.DBclass.Terrain(db,a)
            if temp <= terr.maxtemp and temp >= terr.mintemp  and umid <= terr.maxhmd and umid >= terr.minhmd:
                terrain.append(terr)
            a=a+1

        terrain.append(None)


        indexa=random.randint(0,len(animal)-1)
        indexv=random.randint(0,len(vegetal)-1)
        indext=random.randint(0,len(terrain)-1)
        if gxel not in self.content.keys() :
            self.content[gxel]={}

        self.content[gxel][xel]=(animal[indexa],vegetal[indexv],terrain[indext])

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

"""TODO: 
-GESTISCI NONE 
-RETURNA CONTENUTO DI UNA CELLA DI CONTENT
-
"""









