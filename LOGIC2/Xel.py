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
                self.exa=Exa(origin.e,origin.x+1,origin.a-1)
            elif direction=="d":
                self.exa=Exa(origin.e-1,origin.x+1,origin.a)
            elif direction=="s":
                self.exa=Exa(origin.e-1,origin.x,origin.a+1)
            elif direction=="a":
                self.exa=Exa(origin.e,origin.x-1,origin.a+1)
        else :
            self.exa=Exa()

    @staticmethod
    def newHex(radius):
        org = Xel()
        temporg = org
        index=("q","w","e","d","s","a")
        #first step
        laststep=-1
        lastxel=None
        end=false
        while end==false :
            if lastxel==None:
                lastxel=temporg.dir[index[laststep+1]]=xel(temporg,index[laststep+1])
            else:
                temporg.dir[index[laststep+1]]=lastxel

            if lastxel.dir[index[laststep+2]]==None:
                lastxel=lastxel.dir[index[laststep+2]]=xel(lastxel,index[laststep+2])
                if lastxel.exa.e>radius and lastxel.exa.x>radius and lastxel.exa.a>radius:

                lastxel.dir[index[laststep+4]]=temporg
            else:
                temporg=lastxel.dir[index[laststep+2]]=temporg.dir[index[laststep+1]]

            laststep+=1
            if laststep<=6:
                laststep-=6

                        
                
        return org

