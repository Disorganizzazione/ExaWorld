import json
import os

def save(dictionary):
    if not os.path.exists("json_files"):
        os.makedirs("json_files")
    #with open("json_files/coordinates.json", "w") as fp:
        #json.dump(dictionary, fp)
    data = open("json_files/coordinates.json", "w")
    data.write("{ ")
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    for i in range(0,len(dictionary)-2):
        data.write('"' + keys[i] + '"' + ':' + '"' + str(values[i]) + '"')
        data.write(', ')
    data.write('"' + keys[len(dictionary)-1] + '"' + ':' + '"' + str(values[len(dictionary)-1]) + '"')
    data.write("}")
    data.close()

def load(filepath):
    with open(filepath, "r") as fp:
        obj = json.load(fp)
        return(obj)

data = dict([
    ("terrain","forest"),
    ("creature","rabbit"),
    ("strength",6),
    ("type","a")
])
save(data)
obj = load("json_files/coordinates.json")
print(obj["terrain"])

