#!/usr/bin/python
#

import sys
import pygame
from pygame.locals import *

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print "ERROR: PyOpenGL not installed properly."


class Demo(object):
    # Run flag
    stop = False
    
    # Screen
    size = (640,480)
    flags = OPENGL|DOUBLEBUF|HWSURFACE

    # Camera/Eye
    eye_x = 0.0
    eye_y = 0.0
    eye_z = 100
    

    def __init__(self):
        # Initialise pygame
        pygame.init()
        self.screen = pygame.display.set_mode(self.size,self.flags)
        self.clock = pygame.time.Clock()

        # Initialise the OpenGL stuff
        glViewport(0, 0, self.size[0], self.size[1])
        glDisable(GL_DEPTH_TEST)
        

    def handle_keys(self, keys):
        if keys[K_SPACE]:
            self.stop = True

    def handle_events(self, events):
        eye_changed = False
        for event in events:
            if event.type == QUIT:
                self.stop = True
            if event.type == MOUSEBUTTONDOWN:
                eye_changed = True
                if event.button == 4:
                    self.eye_z += 10
                if event.button == 5:
                    self.eye_z -= 10
            if event.type == MOUSEMOTION:
                (dx, dy) = pygame.mouse.get_rel()
                self.eye_x += dx
                self.eye_y += dy
                eye_changed = True

        if eye_changed:
#            print "Eye=(%f, %f, %f)" % (self.eye_x, self.eye_y, self.eye_z)
            print "Pos=(%f, %f)" % pygame.mouse.get_pos();
        
    def clear_screen(self):
        # black screen
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClear(GL_DEPTH_BUFFER_BIT|GL_COLOR_BUFFER_BIT)

    def update_screen(self):
        pygame.display.flip()

    def sync(self):
        glFinish()

    def set_camera(self):

        # How we project the scene
        glMatrixMode (GL_PROJECTION);
        glLoadIdentity ();
        (x, y) = pygame.mouse.get_pos();
        xoff = self.size[0]/2
        yoff = self.size[1]/2
        glOrtho (-xoff+x, +xoff+x,
                 -yoff+y, +yoff+y,
                 0, 1);

        
    def draw_screen(self):
        glMatrixMode (GL_MODELVIEW);
        
        glColor3f (1.0, 1.0, 1.0)

        glBegin(GL_POLYGON)
        glVertex3i(200,100, 0)
        glVertex3i(-200,100, 0)
        glVertex3i(-200,-100, 0)
        glVertex3i(200,-100, 0)
        glEnd()

        glBegin(GL_POLYGON)
        glVertex3i(200,200, 0)
        glVertex3i(300,300, 0)
        glVertex3i(400,200, 0)
        glEnd()

        glFlush()

    # The main run loops
    def run(self):
        while not self.stop:
            self.clock.tick()
            self.handle_events(pygame.event.get())
            self.handle_keys(pygame.key.get_pressed())
            self.clear_screen()
            self.set_camera()
            self.draw_screen()
            self.update_screen()
            self.sync()

        self.finish()

    def finish(self):
        print self.clock.get_fps()
        pygame.quit()
        
  

if __name__ == "__main__":
    demo = Demo()
    demo.run()


