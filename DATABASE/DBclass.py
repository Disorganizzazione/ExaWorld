import psycopg2

class ExaDB(): #insieme delle strutture contenenti gli elementi del database
    def __init__(self):
        
        conn = psycopg2.connect("dbname=exaworld user=postgres") #connessione database
        cur = conn.cursor()                                     #cursore per eseguire le query sul database
        cur.execute("select * from world.terreno", vars = None)
        self.terrains = cur.fetchall()                          #una volta visualizzate le tabelle, ognuna viene trasformata in una lista di liste
        cur.execute("select * from world.creature", vars = None)
        self.creatures = cur.fetchall()                         #fetchall() permette di prelevare tutte le righe in una sola volta
        #print(self.creatures[1][8])
        cur.execute("select * from world.erbivoro", vars = None)
        self.herbivores = cur.fetchall()
        cur.execute("select * from world.carnivoro", vars = None)
        self.carnivores = cur.fetchall()
        cur.execute("select * from world.comportamento", vars = None)
        self.behaviours = cur.fetchall()

class Creature():   #classe creatura dinamica che può essere usata sia tramite iterazione per istanziare tutte le creature, sia per crearne una specifica con le caratteristiche del database
    def __init__(self,database,id):
        index = id-1
        self.nome = database.creatures[index][1]    #usa le strutture della classe ExaDB per raccogliere i dati dell'oggetto
        self.prede = []
        #if database.creatures[id][2] > 0:
        #    self.comportamento = database.behaviours[database.creatures[id][2]][1]
        #   self.ferocia = database.behaviours[database.creatures[id][2]][2]
        #   self.branco = database.behaviours[database.creatures[id][2]][3]
         #   self.sedentarieta = database.behaviours[database.creatures[id][2]][4]
         #   self.riproduzione = database.behaviours[database.creatures[id][2]][5]
        #else:
        #    self.riproduzione = database.behaviours[database.creatures][id][3]
        if database.creatures[index][4] == "a":                     #distingue tra animale e vegetale
            self.tipo = "animale"
            #print("-------------------------------------------------------")
            self.comportamento = database.behaviours[database.creatures[index][2]-1][1]
            #print (str(database.behaviours[database.creatures[index][2]-1][1]))
            self.ferocia = database.behaviours[database.creatures[index][2]-1][2]
            #print(str(database.behaviours[database.creatures[index][2]-1][2]))
            self.branco = database.behaviours[database.creatures[index][2]-1][3]
            #print(str(database.behaviours[database.creatures[index][2]-1][3]))
            self.sedentarieta = database.behaviours[database.creatures[index][2]-1][4]
            #print(str(database.behaviours[database.creatures[index][2]-1][4]))
            self.riproduzione = database.behaviours[database.creatures[index][2]-1][5]
            #print(str(database.behaviours[database.creatures[index][2]-1][5]))
            #print("------------------------------------------------------")
        else:
            #print("hey")
            self.tipo = "vegetale"
            self.riproduzione = database.creatures[index][3]
            #print("her")

        self.resistenza = database.creatures[index][5]
        if self.tipo == "animale":
            self.forza = database.creatures[index][6]               #forza viene assegnata solo se animale
            self.velocita = database.creatures[index][7]            #velocità viene assegnata solo se animale
        if database.creatures[index][8] == "e" :                     #risale tutte le chiavi esterne a seconda di se erbivoro o carnivoro e crea una lista delle prede
            for i in database.herbivores :
                if id == i[0]:
                    self.prede.append(database.creatures[i[1]-1][1])
        if database.creatures[index][8] == "c" :
            for i in database.carnivores :
                if id == i[0]:
                    self.prede.append(database.creatures[i[1]-1][1])
                    #print(str(database.creatures[i[1]-1][1]))
                    #print(database.creatures[database.carnivores[i-1][1]][1])

        #if database.creatures[id][8] == "c":
            #for i in range(0,len(database.carnivores)):
                #if id+1== database.carnivores[i][0]:
                    #self.prede.append(database.creatures[database.carnivores[i][1]][1])

        self.mintemp = database.creatures[index][9]
        #print(str(self.mintemp) +" uguale " + str(database.creatures[index][9]))
        self.maxtemp = database.creatures[index][10]
        self.minhmd = database.creatures[index][11]
        self.maxhmd = database.creatures[index][12]
        #print(database.creatures[index][8])

class Terrain():
    def __init__(self,database,id):
        index = id-1
        self.nome = database.terrains[index][1]
        self.mintemp = database.terrains[index][2]
        self.maxtemp = database.terrains[index][3]
        self.minhmd = database.terrains[index][4]
        self.maxhmd = database.terrains[index][5]