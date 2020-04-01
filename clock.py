#!/usr/bin/env python3
# Pygame Clock
# Created by Samuel Davenport

NAME = 'Clock'
__version__ = '0.0.1'

SCREENSIZE = (800, 600)
FPS = 60

from pygame.locals import *
import pygame
from Vector2 import Vector2
import utils
from math import sin, cos, radians
import time

class Sprite(object):
    def __init__(self, image_filename, position, name='', alpha=True):
        self.name = name
        self.position = position
        self.image = pygame.image.load(image_filename)
        if alpha:
            self.image.convert_alpha()
        else:
            self.image.convert()
    
    def __repr__(self):
        x, y = self.position
        return '<Sprite %s at %i, %i>' % (self.name, x, y)
    
    def render(self, surface):
        # Render at the center of image
        w, h = self.image.get_size()
        x, y = self.position
        x -= w/2
        y -= h/2
        surface.blit(self.image, (x, y))
    
    def collision(self, point):
        # Return True if a point is over image
        point_x, point_y = point
        x, y = self.position
        w, h = self.image.get_size()
        x -= w/2
        y -= h/2
        
        in_x = point_x >= x and point_x < x + w
        in_y = point_y >= y and point_y < y + h
        
        return in_x and in_y
    pass

def move_deg(deg, dist, plus=(0, 0)):
    rad = radians(deg)
    plus = Vector2(*plus)
    return utils.roundl( *list( plus + (Vector2(sin(rad), cos(rad)) * dist) ) )

def make_num_sprites():
    middle = Vector2(*utils.amol(SCREENSIZE, d=2))
    pos = []
    for i in range(12):
        deg = (30 * (i+1))
        pos.append(move_deg(deg, 200, middle))
    
    sprites = []
    for i in range(12):
        num = str(12 - ((7 + i) % 12))
        #num = str(i+1)
        sprites.append(Sprite('pic/'+num+'.png', pos[i], num))
    return sprites

def run():
    global sprites
    # Initialize the 44KHz 16-bit stereo sound
    pygame.mixer.pre_init(44100, -16, 2, 1024*4)
    pygame.init()
    
    screen = pygame.display.set_mode(SCREENSIZE, 0)
    pygame.display.set_caption(NAME)
    
    background = pygame.surface.Surface(SCREENSIZE).convert()
    middle = Vector2(utils.roundl(*utils.amol(SCREENSIZE, d=2)))
    
    Sprite('pic/background.png', utils.amol(SCREENSIZE, d=2), 'Background',
           False).render(background)
    pygame.draw.circle(background, [0]*3,   middle, 260)
    pygame.draw.circle(background, [255]*3, middle, 230)
    
    for sprite in make_num_sprites():
        sprite.render(background)
    
    RUNNING = True
    
    clock = pygame.time.Clock()
    
    while RUNNING:
        button_pressed = None
        for event in pygame.event.get():
            if event.type == QUIT:
                RUNNING = False
        
        screen.unlock()
        
        screen.fill([255]*3)
        screen.blit(background, (0,0))
        
        h, m, s = utils.intl(*' '.join(time.asctime().split('  ')).split(' ')[3].split(':'))
        h %= 12
        h *= 30
        m *= 6
        s *= 6
        #h, m, s = utils.amol([h, m, s], s=180)
        
        hpos = Vector2(move_deg(180-h, 120, middle))
        mpos = Vector2(move_deg(180-m, 160, middle))
        spos = Vector2(move_deg(180-s, 200, middle))
        
        pygame.draw.line(screen, (255, 0, 0), middle, spos, 10)
        pygame.draw.line(screen, [0]*3, middle, mpos, 10)
        pygame.draw.line(screen, [0]*3, middle,hpos, 10)
        
        b = Vector2(1,1)
        pygame.draw.circle(screen, (255, 0, 0), spos+b, 5)
        pygame.draw.circle(screen, [0]*3, mpos+b, 5)
        pygame.draw.circle(screen, [0]*3, hpos+b, 5)
        pygame.draw.circle(screen, [2]*3, middle+b, 5)
        
        screen.lock()
        
        clock.tick(FPS)
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    run()
