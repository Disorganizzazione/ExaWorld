
import math
from OpenGL.GL import *
from OpenGL.GLU import *


class GraphicHexagon:

    def __init__(self, center, size,
                 pointy_top=False, filled=False,
                 color=(1.0, 1.0, 1.0, 1.0),
                 line_thickness=1, text=""):

        self.__center = center
        self.__size = size
        self.__pointy_top = bool(pointy_top)
        self.__filled = bool(filled)
        self.__color = color
        self.__line_thickness = line_thickness
        self.__text = text
        self.__drawn = False

    def set_center(self, new_center):
        self.__center = new_center

    def get_center(self):
        return self.__center

    def set_size(self, new_size):
        self.__size = new_size

    def get_size(self):
        return self.__size

    def set_pointy_top(self, new_pointy_top):
        self.__pointy_top = new_pointy_top

    def get_pointy_top(self):
        return self.__pointy_top

    def set_filled(self, new_filled):
        self.__filled = bool(new_filled)

    def get_filled(self):
        return self._filled

    def set_color(self, color):
        self.__color = color

    def get_color(self, color):
        return self.__color

    def set_line_thickness(self, new_line_thickness):
        self.__line_thickness = new_line_thickness

    def get_line_thickness(self):
        return self.line_thickness

    def set_text(self, txt):
        self.__text = txt

    def is_drawn(self):
        return self.__drawn

    def draw(self):
        glLoadIdentity()

        if self.__filled:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

        glColor4fv(self.__color)
        glLineWidth(self.__line_thickness)

        glBegin(GL_POLYGON)

        for i in range(6):

            if self.__pointy_top:
                angle = (60 / 180.0) * math.pi * i
            else:
                angle = ((30 / 180.0) * math.pi) + (60 / 180.0) * math.pi * i

            glVertex2d(self.__center[0] +
                       self.__size * math.sin(angle),
                       self.__center[1] +
                       self.__size * math.cos(angle))
        glEnd()

        self.__drawn = True
