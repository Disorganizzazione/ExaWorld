from direct.showbase.ShowBase import ShowBase
from panda3d.core import VBase4
from opensimplex import OpenSimplex
import math

switch_exa = {
        "green": "Exa.egg",
        "red": "Exa_red.egg",
        "yellow": "Exa_yellow.egg",
        "brown": "Exa_brown.egg",
        "blue": "Exa_blue.egg"
        }
openS = OpenSimplex(42) #temporary

class Model:

    @staticmethod
    def loadExaTile(self, x, y, z, type):
        #temporary randomizing
        height = openS.noise2d(x,y) + (math.sqrt(x*x+y*y)-2)/5
        #temporary
        if type == "green":
            if height > 3: 
                type = "brown"
            elif height<0:
                type = "blue"

        self.obj1 = self.loader.loadModel("GRAPHIC/Models/"+ switch_exa[type])
        self.obj1.reparentTo(self.render)
        self.obj1.setPos(x, y, height)
        return self.obj1

    def loadCharacter(self, x, y, z):
        self.char = self.loader.loadModel("GRAPHIC/Models/Char.egg")
        self.char.reparentTo(self.render)
        self.char.setPos(x, y, z)
        return self.char
