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
            print(str(creatures.nome)+ "--------------------------------------------------")
            print(str(creatures.mintemp) +"   "+ str(temp) +"    "+ str(creatures.maxtemp) )
            print(str(creatures.minhmd) +"   "+ str(umid) +"    "+ str(creatures.maxhmd) )
            if creatures.tipo== "vegetale":
                if temp <= creatures.maxtemp and temp >= creatures.mintemp  and umid <= creatures.maxhmd and umid >= creatures.minhmd:
                    vegetal.append(creatures)
            else:
                if temp <= creatures.maxtemp and temp >= creatures.mintemp  and umid <= creatures.maxhmd and umid >= creatures.minhmd:
                    animal.append(creatures)
            animal.append(None)
            vegetal.append(None)
            a=a+1
        a=1
        for i in db.terrains:
            terrains=DBclass.Terrain(db,a)
            if temp <= creatures.maxtemp and temp >= creatures.mintemp  and umid <= creatures.maxhmd and umid >= creatures.minhmd:
                terrain.append(terrains)
            terrain.append(None)
            #print(terrains.nome)
            a=a+1
        
        indexa=random.randint(0,len(animal)-1)
        indexv=random.randint(0,len(vegetal)-1)
        indext=random.randint(0,len(terrain)-1)
        print("\n\n\n\n")
        print(len(animal),len(vegetal),len(terrain))
        print(indexa,indext,indexv)

        if gxel not in self.content.keys() :
            self.content[gxel]={}

        self.content[gxel][xel]=(animal[indexa],vegetal[indexv],terrain[indext])



a=content()
a.creation((0,0,0),(1,3,2),20,20)
a.creation((0,0,0),(1,4,2),20,20)
a.creation((0,1,0),(1,3,2),20,20)

print(a.content)








