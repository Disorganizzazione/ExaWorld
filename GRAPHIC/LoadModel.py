from direct.showbase.ShowBase import ShowBase
from panda3d.core import VBase4

switch_exa = {
        "green": "Exa.egg",
        "red": "Exa_red.egg",
        "yellow": "Exa_yellow.egg"
    }

class Model:

    @staticmethod
    def loadExaTile(self, x, y, z, type):
        self.obj1 = self.loader.loadModel("GRAPHIC/Models/"+ switch_exa[type])
        self.obj1.reparentTo(self.render)
        self.obj1.setPos(x, y, z)
        return self.obj1

    def loadCharacter(self, x, y, z):
        self.char = self.loader.loadModel("GRAPHIC/Models/Char.egg")
        self.char.reparentTo(self.render)
        self.char.setPos(x, y, z)
        return self.char
