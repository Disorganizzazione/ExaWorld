import json
import os

def save(dictionary, coordinates):                   #funzione che salva su un file json un dizionario
    if not os.path.exists("json_files"):    #crea la cartella se non esiste
        os.makedirs("json_files")
    data = open("json_files/" + str(coordinates) + ".json", "w")
    data.write("{ ")
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    for i in range(0,len(dictionary)-1):        #scrivi il dizionario in sintassi json
        data.write('"' + str(keys[i]) + '"' + ':' + '"' + str(values[i]) + '"')
        data.write(', ')
    data.write('"' + str(keys[len(dictionary)-1]) + '"' + ':' + '"' + str(values[len(dictionary)-1]) + '"')
    data.write("}")                             #niente virgola sull'ultimo elemento
    data.close()

def load(filename):             #funzione che carica un file json da un percorso
    try:
        fp = open("json_files/" + str(filename), "r")
        obj = json.load(fp)
        return(obj)
    except FileNotFoundError:
        return(-1)
    except:
        return("brutto errore")

