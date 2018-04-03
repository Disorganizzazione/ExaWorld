from Exa import *

class Xel:
    def __init__(self, origin=None, direction=None):
        self.values=None
        self.exa=None
        self.link= {'q':None,'w':None,'e':None,'d':None,'s':None,'a':None}

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
        tmp_or = origin #scan every xel
        next_or = origin  #change origin after a final step
        lastXel=None #last created exa
        index=list(origin.link.keys())  # index of directions

        #BASIC CASE
        lastXel= tmp_or.link['q'] = Xel(origin.exa, 'q') #first link (new exa)
        tmp_or=lastXel
        lastXel= tmp_or.link['e']= Xel(lastXel.exa,'e') #second link (new exa)
        tmp_or=lastXel
        tmp_or.link['s']= origin #last link (existing exa)
        tmp_or=origin

        i=0
        j=0
        while(j<6*radius*radius-1):
            i+=1
            j+=1
            #STANDARD/FINAL FIRST LINK CASE
            tmp_or.link[index[i%6]]=lastXel #first link (existing exa)
            tmp_or=lastXel
            #STANDARD CASE         
            if next_or.link[index[(i+1)%6]]==None:   
                lastXel= tmp_or.link[index[(i+2)%6]]= Xel(lastXel.exa, index[(i+2)%6]) #second link (new exa)
                tmp_or=lastXel
                tmp_or.link[index[(i+4)%6]]=next_or #last link (existing exa)
                tmp_or=next_or
                continue #not a final case
            #FINAL CASE
            tmp_or.link[index[(i+2)%6]]= next_or.link[index[(i+1)%6]] #second link (existing exa)
            tmp_or= next_or.link[index[(i+1)%6]]
            tmp_or.link[index[(i+4)%6]]=next_or #last link (existing exa)
            next_or=tmp_or #change origin for next cycle
            i-=2

        tmp_or=lastXel # set temp_or on the edge
        i=1
        
        while(i<=6): #create external links
            if tmp_or.link[index[i%6]]==None: 
                i+=1 #change direction
            else:
                tmp_or.link[index[i%6]].link[index[(i+3)%6]]= tmp_or #go back
                tmp_or =tmp_or.link[index[i%6]] #create link
        return origin          


 
 