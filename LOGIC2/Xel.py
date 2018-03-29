from Exa import *

class Xel:
    def __init__(self, origin=None, direction=None):
        self.values=None
        
        self.exa=None
        self.dir=dict()

        #self.dir["q"]=None
        #self.dir["w"]=None
        #self.dir["e"]=None
        #self.dir["d"]=None
        #self.dir["s"]=None
        #self.dir["a"]=None

        if origin != None and direction != None :
            if direction=="q" :
                self.exa=Exa(origin.e+1,origin.x-1,origin.a)
            elif direction=="w":
                self.exa=Exa(origin.e+1,origin.x,origin.a-1)
            elif direction=="e":
                self.EXA=Exa(origin.e,origin.x+1,origin.a-1)
            elif direction=="d":
                self.EXA=Exa(origin.e-1,origin.x+1,origin.a)
            elif direction=="s":
                self.EXA=Exa(origin.e-1,origin.x,origin.a+1)
            elif direction=="a":
                self.EXA=Exa(origin.e,origin.x-1,origin.a+1)
        else :
            self.exa=Exa()

    @staticmethod
    def newHex(radius):
        org = Xel()
        temporg = org
        #first step
        temporg.q=Xel(temporg,"q")
        temporg.q.e=Xel(temporg.q,"e")
        temporg.q.e.s=temporg

        laststep="q"
        lastxel=temporg.q.e.s
        end=false
        while end==false :
            pass
        return org

