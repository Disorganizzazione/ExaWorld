
class Exa:

    # The argument of constructor should be a single Exa object or 3 int
    def __init__(self, *args):
        # Constructor with 1 parameter, Exa object
        if len(args) == 1 and isinstance(args[0], Exa):
            self.e = args[0].e
            self.x = args[0].x
            self.a = args[0].a
        # Constructor with 3 parameters, if they're all int
        elif len(args) == 3 and all(isinstance(a, int) for a in args):
            self.e = args[0]
            self.x = args[1]
            self.a = args[2]
            self.redux()
        elif len(args) >= 4 :
            print("terribile errore")
        else:
            self.e = 0
            self.x = 0
            self.a = 0

    # TODO: da controllare se i 3 seguenti getter servono anche in python
    def get_e(self):
        return self.e

    def get_x(self):
        return self.x

    def get_a(self):
        return self.a

    # turn 3 numbers into an Exa object
    @staticmethod
    def vector(e, x, a):
        return Exa(e, x, a)

    # coordinates reducer to a minimal form
    def redux(self):
        # find the coord with intermediate value
        # sorting the [e,x,a] array and taking the middle value
        redx = sorted([self.e, self.x, self.a])[1]
        # reduce coordinates
        self.e -= redx
        self.x -= redx
        self.a -= redx

    # returns the "distance" of the Exa from the origin
    def module(self):
        return abs(self.e) + abs(self.x) + abs(self.a)

    # returns an Exa which is the sum of the current + exa
    def add(self, exa):
        if isinstance(exa, Exa):
            return Exa(self.e+exa.e,
                       self.x+exa.x,
                       self.a+exa.a)
        else:
            # invalid parameter, Exa object required
            pass

    # return an Exa which is the origin-specular version of the current Exa
    def inv(self):
        return Exa(-self.e,
                   -self.x,
                   -self.a)

    # returns an Exa which coordinates are equal to current - exa
    def diff(self, exa):
        if isinstance(exa, Exa):
            return Exa(self.inv().add(exa).inv())
        else:
            # invalid parameter, Exa object required
            pass

    # 6 directions movement methods
    # TODO: forse si può evitare di fare 6 metodi, ne farei 1 solo.
    # TODO: Esempio: move_to('lettera') con uno switch/case
    def w(self):
    def w_(self):
        self.x -= 1
        self.redux()
    def e(self):
    def e_(self):
        self.e += 1
        self.redux()
    def d(self):
    def d_(self):
        self.a -= 1
        self.redux(cambiamenti vari a Exa.py)
    def x(self):
        self.redux()
    def x_(self):
        self.x += 1
        self.redux()
    def z(self):
    def z_(self):
        self.e -= 1
        self.redux()
    def a(self):
    def a_(self):
        self.a += 1
        self.redux()
