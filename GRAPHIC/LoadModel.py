from direct.showbase.ShowBase import ShowBase
from panda3d.core import VBase4


class Model:
    @staticmethod
    def loadModels(self, x, y, z):
        self.obj1 = self.loader.loadModel("GRAPHIC/Models/Exa.egg")
        self.obj1.reparentTo(self.render)
        self.obj1.setPos(x, y, z)
        return self.obj1

    def loadCharacter(self, x, y, z):
        self.char = self.loader.loadModel("GRAPHIC/Models/Char.egg")
        self.char.reparentTo(self.render)
        self.char.setPos(x, y, z)
        return self.char
