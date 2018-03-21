class Exa():
    E, X, A
    def __init__(self,E=0,X=0,A=0):
        if E.isInteger():
            self.E = E
            self.X = X
            self.A = A
            self.redux()
        #serve un altro controllo
		# isinstance(E, Exa)
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
        #temp = sorted([E,X,A])
