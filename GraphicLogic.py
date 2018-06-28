from direct.showbase.ShowBase import ShowBase

from GRAPHIC import LoadLight, LoadModel
from LOGIC import *
#from LOGIC import Exa, Xel, Map

apo=0.86603
r=1

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.light= LoadLight.Light
        self.model=LoadModel.Model
        
        self.light.setupLight(self)
        self.model.loadModels(self, -3, 7, 5)
        self.model.loadModels(self, -3+apo, 7+r*1.5, 5)
        #Prospettiva??????????
       #self.useDrive()


app = MyApp()
app.run()
