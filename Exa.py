class Exa():
    E=None
    X=None
    A=None
    
    def __init__(self, gon=None, E=None,X=None,A=None):
        if gon is None:
            if (E == None and X==None and A==None):
                E=0
                X=0
                A=0
            else:
                self.E=E
                self.X=X
                self.A=A
                self.redux()      
        else:
            E= gon.E
            X= gon.X
            A= gon.A
            
    def redux(self):
        pass
    
    




