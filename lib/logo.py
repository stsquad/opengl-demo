#!/usr/bin/python
#

from math import radians, sin, pi

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
    
    def __init__(self, size_x, size_y):
        self.counter = 0
        self.size_x = size_x
        self.size_y = size_y

    def next(self):
        self.counter += 1

    def draw(self, pos_x, pos_y):
        
        glBegin(GL_QUADS)
        glVertex3f(pos_x, pos_y, 0)
        glVertex3f(pos_x+self.size_x, pos_y, 0)
        glVertex3f(pos_x+self.size_x, pos_y+self.size_y, 0)
        glVertex3f(pos_x, pos_y+self.size_y, 0)
        glEnd()
