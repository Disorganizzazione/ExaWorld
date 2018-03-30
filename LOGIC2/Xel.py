from Exa import *
#from copy import copy, deepcopy

class Xel:
    def __init__(self, origin=None, direction=None):
        self.values=None
        
        self.exa=None
        self.link= {'q':None,'w':None,'e':None,'d':None,'s':None,'a':None}

        #self.link["q"]=None
        #self.link["w"]=None
        #self.link["e"]=None
        #self.link["d"]=None
        #self.link["s"]=None
        #self.link["a"]=None

        if origin != None and direction != None :
            if direction == "q" :
                self.exa= origin.Q()
            elif direction == "w":
                self.exa= origin.W()
            elif direction == "e":
                self.exa= origin.E()
            elif direction == "d":
                self.exa= origin.D()
            elif direction == "s":
                self.exa= origin.S()
            elif direction == "a":
                self.exa= origin.A()
        else:
            self.exa=Exa()

    def __str__(self):
        return Exa.__str__(self.exa) + f" -> [   q: {self.link['q'].exa if self.link['q']!=None else None},   w: {self.link['w'].exa if self.link['w']!=None else None},   e: {self.link['e'].exa if self.link['e']!=None else None},   d: {self.link['d'].exa if self.link['d']!=None else None},   s: {self.link['s'].exa if self.link['s']!=None else None},   a: {self.link['a'].exa if self.link['a']!=None else None}   ]"
#q,w,e,d,s,a
#0,1,2,3,4,5
    @staticmethod
    def newHex(radius):
        origin = Xel()
        tmp_or = origin
        tmp_or = origin 
        #first step
        #######????dic_i=list(origin.link.keys())
        ls=-1 #last step
        lastXel=None
        #end=False

        #Basic case
        #print("or", tmp_or, "\nlast", lastXel,"\n")
        lastXel= tmp_or.link['q'] = Xel(origin.exa, 'q') #first link
        print("or", tmp_or, "\nlast", lastXel,"\n")
        tmp_or=lastXel
        lastXel= tmp_or.link['e']= Xel(lastXel.exa,'e') #second link
        print("or", tmp_or, "\nlast", lastXel,"\n")
        tmp_or=lastXel
        lastXel= tmp_or.link['s']= origin #last link
        print("or", tmp_or, "\nlast", lastXel,"\n")
        tmp_or=lastXel
        
        lastXel = tmp_or.link['w'] = Xel(lastXel.exa,'w') #ultimo link (s)
        print("or", tmp_or, "\nlast", lastXel,"\n")
        tmp_or=lastXel

        while(radius!=0):
            for i, xdir in enumerate(origin.link.keys()):
                print(i,xdir)
            radius-=1      

        return origin          
        
        

    @staticmethod
    def triangle(i, origin):
        pass


origin = Xel.newHex(5)
print(origin)