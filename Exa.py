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
            
    def redux(self): 
        pass
    
    




