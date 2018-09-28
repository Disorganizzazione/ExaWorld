import random


class ExaRandom:

    @staticmethod
    def randomize_vertices(self):
        rnd_list = [(0, 10)] * 80 + [(11, 40)] * 15 + [(41, 100)] * 5
        result = []
        for i in range(0, 6):
            chosen = random.choice(rnd_list)
            result.append(random.randint(chosen[0], chosen[1]) / 10 * random.choice([-1, 1]))
        return result

    def interpolate(self, vABC, exaA, exaB, exaC, exaP):
        (vA,vB,vC) = vABC


        return
