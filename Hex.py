
class Hex:

    # Constructor to create new cells
    def __init__(self, radius=0):
        """TODO descrizione"""

        if not isinstance(radius, int):
            radius = 0
        self.radius = radius
        self.origin = Xel()

        temp = self.origin
        for r in range(radius):
            # first one
            if r > 0:
                temp = temp.link(6)
                for l in range(r-1):
                    temp = temp.link(16)
            # 4 slices
            for v in range(1,5):
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

    def act(self):
        """TODO descrizione"""
        temp = origin
        temp.law()
        for r in range(radius-1):
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
        temp = origin
        temp.time()
        for r in range(radius-1):
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
        temp = origin
        temp.kill()
        for r in range(radius-1):
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
                temp.kill()

    def print(self):
        """TODO descrizione"""
        ra = radius + 1
        vector = Exa(0, -radius, 0)

        # TODO: check if cycle is correct
        for i in range(-radius, radius+1):
            for j in range(abs(i)):
                print(" ")
            temp = origin.access(vector.inv())
            for j in range(ra):
                str = ". "
                if temp.getLife():
                    str = "o "
                print(str)
                temp = temp.d
            if i < 0:
                vector.z()
                ra += 1
            else:
                vector.x()
                ra -= 1
            print("\n")
