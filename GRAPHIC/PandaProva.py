from direct.showbase.ShowBase import *

class Window(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.loadModels()

    def loadModels(self):
        path="untitled.egg"
        self.ttc= loader.loadModel(path)
        self.ttc.reparentTo(render)

game= Window()
game.run()
