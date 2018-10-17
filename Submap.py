from LOGIC import Xel

class Submap:
    def __init__(self, centerXY, array_Z=[0,0,0,0,0,0,0], array_T=[0,0,0,0,0,0,0], array_H=[0,0,0,0,0,0,0], noise_seed=0):
        self.centerXY = centerXY#(centerXY[0].__round__(1), centerXY[1].__round__(1))
        self.array_Z = array_Z
        self.array_T = array_T
        self.array_H = array_H
        self.noise_seed = noise_seed
        self.node = None

    def __str__(self):
        return str(self.centerXY)+" NodePath: "+str(self.node)