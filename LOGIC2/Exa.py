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

<<<<<<< HEAD
=======
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
    
    
    
exa1=Exa(2,0,-2)
exa1=Exa(3,0,-3)
exa2=Exa(-1,1,0)
print(len(exa1))    
print(exa1.distance(exa2))    
>>>>>>> ef9d7c210910209019ec100c2cd9decb1eceb05e
        
            
