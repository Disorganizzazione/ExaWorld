from Xel import *
class Exa:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], Exa):
            self.e = args[0].e
            self.x = args[0].x
            self.a = args[0].a
        elif len(args) == 3 and all(isinstance(a, int) for a in args):
            self.e = args[0]
            self.x = args[1]
            self.a = args[2]
        else:
            self.e = 0
            self.x = 0
            self.a = 0

    #Invert exa's coordinates
    def __neg__(self):
        return Exa(-self.e, -self.x, -self.a)
    #== e != operators
    def __eq__(self, other):
        return self.e == other.e and self.x == other.x and self.a == other.a
    #+ operator
    def __add__(self, other):
        return Exa(self.e + other.e, self.x + other.x , self.a + other.a)
    #- operator
    def __sub__(self, other):
        return Exa(self.e - other.e, self.x - other.x , self.a - other.a)
     
    # return an Exa which is the origin-specular version of the current Exa
    @staticmethod
    def vector(e, x, a):
        return Exa(e, x, a)
    #print coordinates
    def __str__(self):
        return f"({self.e}, {self.x}, {self.a})"
    #lenght (from origin)
    def __len__(self):
        return int((abs(self.e) + abs(self.x) + abs(self.a))/2)
    #return the distance between two exa
    def distance(self, exa):
        return len(self-exa)
    
    def Q(self):
        self.e=self.e + 1
        self.x = self.x -1
    def W(self):
        self.e=self.e + 1
        self.a = self.a -1
    def E(self):
        self.x=self.x + 1
        self.a = self.a -1
    def D(self):
        self.e=self.e - 1
        self.x = self.x +1
    def S(self):
        self.e=self.e - 1
        self.a = self.a +1  
    def A(self):
        self.x=self.x - 1
        self.a = self.a +1

exa1=Exa()
print(exa1)
exa1.A()
exa1.A()
print(exa1)
        
            
