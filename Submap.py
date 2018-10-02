from LOGIC import Xel

class Submap:
    def __init__(self, centerXY, array_Z=[0,0,0,0,0,0,0], array_T=[0,0,0,0,0,0,0], array_H=[0,0,0,0,0,0,0], noise_seed=0):
        self.centerXY = centerXY
        self.array_Z = array_Z
        self.array_T = array_T
        self.array_H = array_H
        self.noise_seed = noise_seed

    def __str__(self):
        string = ""
        for i in range(7):
            string += "xel {}: Z={}, T={}, H={}, seed={}\n".format(i,self.array_Z[i],self.array_T[i],self.array_H[i],self.noise_seed)
        return "Submap (x,y) = {self.centerXY}\n"+string
        #return Exa.Exa.__str__(self.exa) + f" -> [   q: {self.link['q'].exa if self.link['q']!=None else None},   w: {self.link['w'].exa if self.link['w']!=None else None},   e: {self.link['e'].exa if self.link['e']!=None else None},   d: {self.link['d'].exa if self.link['d']!=None else None},   s: {self.link['s'].exa if self.link['s']!=None else None},   a: {self.link['a'].exa if self.link['a']!=None else None}   ]"
