from panda3d.core import VBase3
import random
import math

vertices_exa = [VBase3(0, -1, 1), VBase3(1, -1, 0), VBase3(1, 0, -1)]  # 'e' and 'a' coords are inverted for GraphicLogic.drawMap() problem

class ExaRandom:

    @staticmethod
    def randomize_vertices(self):
        rnd_list = [(0, 10)] * 80 + [(11, 40)] * 15 + [(41, 100)] * 5
        result = []
        for i in range(0, 6):
            chosen = random.choice(rnd_list)
            result.append(random.randint(chosen[0], chosen[1]) / 10 * random.choice([-1, 1]))
        return result

    def interpolate(self, vABC, radius, exaP):
        (vA, vB, vC) = vABC
        (eP, xP, aP) = exaP
        # TODO: change sign of vertices_exa when opposite
        # TODO: chose vertices_exa[index] for each point P
        (eB, xB, aB) = vertices_exa[1]*radius
        (eC, xC, aC) = vertices_exa[2]*radius
        
        # the influence of each vertex on P scales with the inverse of the distance
        wA = 1 / max(abs(eP), abs(xP), abs(aP))
        wB = 1 / max(abs(eB - eP), abs(xB - xP), abs(aB - aP))
        wC = 1 / max(abs(eC - eP), abs(xC - xP), abs(aC - aP))
        """
        # Barycentric coordinates
        xB_xC = xB-xC
        eC_eB = eC-eB
        eP_eC = eP-eC
        xP_xC = xP-xC
        divisore = xB_xC*-eC + eC_eB*-xC
        wA = (xB_xC*eP_eC + eC_eB*xP_xC) / divisore
        wB = (-xC*eP_eC + -eC*xP_xC) / divisore
        wC = 1 - wA - wB
        """
        return (wA*vA + wB*vB + wC*vC)/(wA+wB+wC)
