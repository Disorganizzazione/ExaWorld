from panda3d.core import VBase3
import random
import math

vertices_exa = [VBase3(1, -1, 0), VBase3(1, 0, -1), VBase3(0, 1, -1)]  # q,w,e (top corners)

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

        vertex_index = 0
        if aP <= 0 and xP < 0:    # qw triangle
            vertex_index = 0
        elif xP >= 0 and eP > 0:  # we triangle
            vertex_index = 1
        elif eP <= 0 and aP < 0:  # ed triangle
            vertex_index = 2
        elif aP >= 0 and xP > 0:  # ds triangle
            vertex_index = 0
            radius = -radius
        elif xP <= 0 and eP < 0:  # sa triangle
            vertex_index = 1
            radius = -radius
        else:  # (eP>=0 and aP>0) # aq triangle
            vertex_index = 2
            radius = -radius

        (eB, xB, aB) = vertices_exa[vertex_index]*radius
        (eC, xC, aC) = vertices_exa[(vertex_index+1)%3]*radius
        
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
