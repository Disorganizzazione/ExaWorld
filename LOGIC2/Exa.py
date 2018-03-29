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
        
        
