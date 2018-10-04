import psycopg2

class ExaDB(): #insieme delle strutture contenenti gli elementi del database
    terrains = []
    creatures = []
    herbivores = []
    carnivores = []
    behaviours = []
    def __init__(self):
        try:
            conn = psycopg2.connect("dbname=exaworld user=postgres") #connessione database
        except:
            print("dbconnection fail")
        cur = conn.cursor()                                     #cursore per eseguire le query sul database
        cur.execute("select * from world.terreno", vars = None)
        self.terrains = cur.fetchall()                          #una volta visualizzate le tabelle, ognuna viene trasformata in una lista di liste
        cur.execute("select * from world.creature", vars = None)
        self.creatures = cur.fetchall()                         #fetchall() permette di prelevare tutte le righe in una sola volta
        cur.execute("select * from world.erbivoro", vars = None)
        self.herbivores = cur.fetchall()
        cur.execute("select * from world.carnivoro", vars = None)
        self.carnivores = cur.fetchall()
        cur.execute("select * from world.comportamento", vars = None)
        self.behaviours = cur.fetchall()

class Creature():   #classe creatura dinamica che può essere usata sia tramite iterazione per istanziare tutte le creature, sia per crearne una specifica con le caratteristiche del database
    def __init__(self,database,id):
        self.nome = database.creatures[id][1]    #usa le strutture della classe ExaDB per raccogliere i dati dell'oggetto
        self.prede = ["boh"]
        if database.creatures[id][2] > 0:
            self.comportamento = database.behaviours[database.creatures[id][2]][1]
            self.ferocia = database.behaviours[database.creatures[id][2]][2]
            self.branco = database.behaviours[database.creatures[id][2]][3]
            self.sedentarieta = database.behaviours[database.creatures[id][2]][4]
            self.riproduzione = database.behaviours[database.creatures[id][2]][5]
        else:
            self.riproduzione = database.behaviours[database.creatures][id][3]
        if database.creatures[id][4] == "a":                     #distingue tra animale e vegetale
            self.tipo = "animale"
        else:
            self.tipo = "vegetale"
        self.resistenza = database.creatures[id][5]
        if self.tipo == "animale":
            self.forza = database.creatures[id][6]               #forza viene assegnata solo se animale
            self.velocita = database.creatures[id][7]            #velocità viene assegnata solo se animale
        if database.creatures[id][8] == "e":                     #risale tutte le chiavi esterne a seconda di se erbivoro o carnivoro e crea una lista delle prede
            for i in range(0,len(database.herbivores)):
                if id+1 == database.herbivores[i][0]:
                    self.prede.append(database.creatures[database.herbivores[i][0]][1])
        if database.creatures[id][8] == "c":
            for i in range(0,len(database.carnivores)):
                if id+1 == database.carnivores[i][0]:
                    self.prede.append(database.creatures[database.carnivores[i][0]][1])
        self.mintemp = database.creatures[id][9]
        self.maxtemp = database.creatures[id][10]
        self.minhmd = database.creatures[id][11]
        self.maxhmd = database.creatures[id][12]