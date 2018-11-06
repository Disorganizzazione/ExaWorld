import json
import os

def save(dictionary):                   #funzione che salva su un file json un dizionario
    if not os.path.exists("json_files"):    #crea la cartella se non esiste
        os.makedirs("json_files")
    data = open("json_files/coordinates.json", "w")
    data.write("{ ")
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    for i in range(0,len(dictionary)-2):        #scrivi il dizionario in sintassi json
        data.write('"' + keys[i] + '"' + ':' + '"' + str(values[i]) + '"')
        data.write(', ')
    data.write('"' + keys[len(dictionary)-1] + '"' + ':' + '"' + str(values[len(dictionary)-1]) + '"')
    data.write("}")                             #niente virgola sull'ultimo elemento
    data.close()

def load(filepath):             #funzione che carica un file json da un percorso
    with open(filepath, "r") as fp:
        obj = json.load(fp)
        return(obj)
