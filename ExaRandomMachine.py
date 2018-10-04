from panda3d.core import VBase3
import Submap
import random
import math

vertices_exa = [VBase3(1, -1, 0), VBase3(1, 0, -1), VBase3(0, 1, -1)]  # q,w,e (top corners)

class ExaRandom:

    def randomize_values(self, number_of_values):
        rnd_list = [(0, 10)] * 80 + [(11, 40)] * 15 + [(41, 100)] * 5
        result = []
        for i in range(0, number_of_values):
            chosen = random.choice(rnd_list)
            result.append(random.randint(chosen[0], chosen[1]) / 10 * random.choice([-1, 1]))
        return result

    def create_submap(self, submapXY):
        rnd_Z = self.randomize_values(7)
        rnd_H = self.randomize_values(7)
        rnd_T = self.randomize_values(7)
        rnd_seed = random.randint(0,100)
        return Submap.Submap(submapXY, rnd_Z, rnd_T, rnd_H, rnd_seed)

    def interpolate(self, vABC, radius, exaP):
        (vA, vB, vC) = vABC
        (eP, xP, aP) = exaP

        vertex_index = None
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
        elif eP >= 0 and aP > 0:  # aq triangle
            vertex_index = 2
            radius = -radius

        (eB, xB, aB) = vertices_exa[vertex_index]*radius
        (eC, xC, aC) = vertices_exa[(vertex_index+1)%3]*radius

        # 1) each vertex influences P according to the inverse of the distance
        wA = 1 / max(abs(eP), abs(xP), abs(aP))
        wB = 1 / max(abs(eB - eP), abs(xB - xP), abs(aB - aP))
        wC = 1 / max(abs(eC - eP), abs(xC - xP), abs(aC - aP))
        """
        # 2) the influence of each vertex on P scales with the inverse of the distance^2
        dA = max(abs(eP), abs(xP), abs(aP))
        dB = max(abs(eB - eP), abs(xB - xP), abs(aB - aP))
        dC = max(abs(eC - eP), abs(xC - xP), abs(aC - aP))
        wA = 1 / pow(dA, 2)
        wB = 1 / pow(dB, 2)
        wC = 1 / pow(dC, 2)
        """
        """
        # 3) the influence of each vertex on P scales with the inverse of the distance, 0 on d=radius
        dA = max(abs(eP), abs(xP), abs(aP))
        dB = max(abs(eB - eP), abs(xB - xP), abs(aB - aP))
        dC = max(abs(eC - eP), abs(xC - xP), abs(aC - aP))
        wA = 1 / dA
        wB = 1 / dB
        wC = 1 / dC
        if dA==radius:
            wA=0
        elif dB==radius:
            wB=0
        elif dC==radius:
            wC=0
        """
        """
        # 4) Barycentric coordinates way (not working correctly, problem on last triangle)
        eB_eC = eB-eC
        xC_xB = xC-xB
        eP_eC = eP-eC
        xP_xC = xP-xC
        divisore = eB_eC*-xC + xC_xB*-eC
        wA = (eB_eC*xP_xC + xC_xB*eP_eC) / divisore
        wB = (eC*xP_xC + -xC*eP_eC) / divisore
        wC = 1 - wA - wB
        """
        return (wA*vA + wB*vB + wC*vC)/(wA+wB+wC)
        
