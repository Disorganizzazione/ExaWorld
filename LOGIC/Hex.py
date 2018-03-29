from Exa import *
from Xel import *
import copy

class Hex:

    # Constructor to create new cells
    def __init__(self, radius=0):
        """TODO descrizione"""

        if not isinstance(radius, int):
            radius = 0
        self.radius = radius
        self.origin = Xel()
        self.position = copy.deepcopy(self.origin.gon)

        temp = copy.deepcopy(self.origin)
        for r in range(radius):
            # first one
            if r > 0:
                temp = temp.link(6)
                for _ in range(r-1):
                    temp = temp.link(16)
            # 4 slices
            for v in range(1, 5):
                if r == 0 and v == 1:
                    temp = temp.link(0)
                else:
                    temp = temp.link(v)
                for l in range(r):
                    temp = temp.link(v + 10)
            # last one
            temp = temp.link(5)
            for l in range(r+1):
                temp = temp.link(15)
    def get_position(self):
        return self.position

    def set_position(self, exa=Exa(0,0,0)):
        self.position = exa

    def __str__(self):
        """TODO descrizione"""
        result = ""
        ra = self.radius + 1
        vector = Exa(0, -self.radius, 0)
        #print(f"Hex.__str__: temp={temp.gon}, position={self.position}\n")
        # TODO: check if cycle is correct
        for i in range(-self.radius, self.radius+1):
            for j in range(abs(i)):
                result += " "
            temp = self.origin.access(vector.inv()) #QUI il problema, tmp è sempre 0,0,0
            print(f"Hex.__str__: temp={temp.gon}, position={self.position}\n")
            for j in range(ra):
                str = "o " if temp.gon.compare(self.position) else ". "
                result += str
                temp = temp.d
            if i < 0:
                vector.z_()
                ra += 1
            else:
                vector.x_()
                ra -= 1
            result += "\n"
        return result

    '''
    def act(self):
        """TODO descrizione"""
        temp = self.origin
        temp.law()
        for r in range(self.radius-1):
            if r > 0:
                temp = temp.move(6)
                temp.law()
                for l in range(r-1):
                    temp = temp.move(1)
                    temp.law()
            for v in range(1,5):
                if r == 0 and v == 1:
                    temp = temp.move(0)
                    temp.law()
                else:
                    temp = temp.move(v)
                    temp.law()
                for l in range(r):
                    temp.move(v + 1)
                    temp.law()
            temp = temp.move(5)
            temp.law()
            for l in range(r+1):
                temp = temp.move(6)
                temp.law()
        temp = self.origin
        temp.time()
        for r in range(self.radius-1):
            if r > 0:
                temp = temp.move(6)
                temp.time()
                for l in range(r-1):
                    temp = temp.move(1)
                    temp.time()
            for v in range(1,5):
                if r == 0 and v == 1:
                    temp = temp.move(0)
                    temp.time()
                else:
                    temp = temp.move(v)
                    temp.time()
                for l in range(r):
                    temp.move(v + 1)
                    temp.time()
            temp = temp.move(5)
            temp.time()
            for l in range(r+1):
                temp = temp.move(6)
                temp.time()

    def reset(self):
        """TODO descrizione"""
        temp = self.origin
        temp.kill()
        for r in range(self.radius-1):
            if r > 0:
                temp = temp.move(6)
                temp.kill()
                for l in range(r-1):
                    temp = temp.move(1)
                    temp.kill()
            for v in range(1,5):
                if r == 0 and v == 1:
                    temp = temp.move(0)
                    temp.kill()
                else:
                    temp = temp.move(v)
                    temp.kill()
                for l in range(r):
                    temp.move(v + 1)
                    temp.kill()
            temp = temp.move(5)
            temp.kill()
            for l in range(r+1):
                temp = temp.move(6)
                temp.kill()'''

#prova
mappa = Hex(2)
print(mappa.get_position())
print(mappa)

mappa.set_position(Exa(1,0,0))
#mappa.origin= mappa.origin.move(1)
print(mappa.get_position())
print(mappa)

mappa.set_position(Exa(1,1,0))
print(mappa.get_position())
print(mappa)

