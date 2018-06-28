from direct.showbase.ShowBase import ShowBase
from panda3d.core import PointLight
from panda3d.core import DirectionalLight
from panda3d.core import AmbientLight
from panda3d.core import VBase4


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.loadModels()
        self.setupLight()
        self.useDrive()

    def setupLight(self):
        primeL= DirectionalLight("prime")
        primeL.setColor(VBase4(.6,.6,.6,1))
        self.light= render.attachNewNode(primeL)
        self.light.setHpr(45,-60,0)
        render.setLight(self.light)
        
        ambL= AmbientLight("amb")
        ambL.setColor(VBase4(.2,.2,.2,1))
        self.ambLight= render.attachNewNode(ambL)
        render.setLight(self.ambLight)
        return

    def loadModels(self):
        self.obj1 = self.loader.loadModel("untitled.egg")
        self.obj1.reparentTo(self.render)
        self.obj1.setPos(-3, 7, 5)

        self.obj2 = self.loader.loadModel("material_box.egg")
        self.obj2.reparentTo(self.render)
        self.obj2.setPos(3, 7, 5)

        self.obj3 = self.loader.loadModel("texture_box.egg")
        self.obj3.reparentTo(self.render)
        self.obj3.setPos(0, 0, 0)

app = MyApp()
app.run()
