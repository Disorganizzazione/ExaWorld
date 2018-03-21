class Exa():
    E, X, A
    
    def __init__(self, gon=None, E=None,X=None,A=None):
        if gon is None:
            self.E = E==None?0:E
            self.X = X==None?0:X
            self.A = A==None?0:A
            self.redux()      
        else:
            self.E = gon.E
            self.X = gon.X
            self.A = gon.A
            
    def vector(self, E, X, A):
        return Exa(, E, X, A)
    
    #coordinates reductor to a minimal form
    def redux(self): 
        redx = 0
        #find the coord with intermediate value
        #if (E<=A and E>=X or E<=X and E>=A)



