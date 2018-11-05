import DBclass
import random

class content():

    def __init__(self):
        self.content={}

    def creation(self, gxel, xel, temp, umid):
        animal=[]
        vegetal=[]
        terrain=[]
        db=DBclass.ExaDB()
        a=1
        for i in db.creatures:
            creatures=DBclass.Creature(db,a)

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
            terrains=DBclass.Terrain(db,a)
            if temp <= creatures.maxtemp and temp >= creatures.mintemp  and umid <= creatures.maxhmd and umid >= creatures.minhmd:
                terrain.append(terrains)
            a=a+1

        terrain.append(None)


        indexa=random.randint(0,len(animal)-1)
        indexv=random.randint(0,len(vegetal)-1)
        indext=random.randint(0,len(terrain)-1)

        if gxel not in self.content.keys() :
            self.content[gxel]={}

        self.content[gxel][xel]=(animal[indexa],vegetal[indexv],terrain[indext])



a=content()
a.creation((0,0,0),(1,3,2),20,20)
a.creation((0,0,0),(1,4,2),20,20)
a.creation((0,1,0),(1,3,2),20,20)

print(a.content)








