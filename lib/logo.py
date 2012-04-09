#!/usr/bin/python
#

import os
from math import radians, sin, pi
from Image import open

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print "ERROR: PyOpenGL not installed properly."


class logo(object):

    counter = 0
    size_x = 0
    size_y = 0
    texture = None
    
    def __init__(self, size_x, size_y, path=None):
        self.counter = 0
        self.size_x = size_x
        self.size_y = size_y

        if path and os.path.exists(path):
            glEnable(GL_TEXTURE_2D)
            image = open(path)
            ix, iy, data = image.size[0], image.size[1], image.tostring("raw", "RGB", 0, -1)

            self.texture = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, self.texture)
            glPixelStorei(GL_UNPACK_ALIGNMENT,1)
            glTexImage2D(GL_TEXTURE_2D, 0, 3,
                         ix, iy, 0,
                         GL_RGB, GL_UNSIGNED_BYTE, data)

            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

            print "logo:__init__ with texture id %d" % (self.texture)

            
    def next(self):
        self.counter += 1

    def draw(self, pos_x, pos_y):
        if self.texture:
            glBindTexture(GL_TEXTURE_2D, self.texture)
            glBegin(GL_QUADS)
            glTexCoord2f(0.0, 0.0);
            glVertex3f(pos_x, pos_y, 0)
            glTexCoord2f(1.0, 0.0);
            glVertex3f(pos_x+self.size_x, pos_y, 0)
            glTexCoord2f(1.0, 1.0);
            glVertex3f(pos_x+self.size_x, pos_y+self.size_y, 0)
            glTexCoord2f(0.0, 1.0);
            glVertex3f(pos_x, pos_y+self.size_y, 0)
            glEnd()
        else:
            glBegin(GL_QUADS)
            glVertex3f(pos_x, pos_y, 0)
            glVertex3f(pos_x+self.size_x, pos_y, 0)
            glVertex3f(pos_x+self.size_x, pos_y+self.size_y, 0)
            glVertex3f(pos_x, pos_y+self.size_y, 0)
            glEnd()
            
