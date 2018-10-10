from direct.showbase.ShowBase import ShowBase
from panda3d.core import PointLight
from panda3d.core import DirectionalLight
from panda3d.core import AmbientLight
from panda3d.core import VBase4

class Light:
    @staticmethod
    def setupLight(self):
        primeL= DirectionalLight("prime")
        primeL.setColor(VBase4(.9,.9,.9,1))
        self.light= render.attachNewNode(primeL)
        self.light.setHpr(45,-60,0)
        render.setLight(self.light)
        
        ambL= AmbientLight("amb")
        ambL.setColor(VBase4(.2,.2,.2,1))
        self.ambLight= render.attachNewNode(ambL)
        render.setLight(self.ambLight)
        return

