#!/usr/bin/env python3
# Simplified Flipped Pygame Clock
# Created by Samuel Davenport

NAME = 'Clock'
__version__ = '0.0.3'

SCREENSIZE = (800, 600)
FPS = 60

from pygame.locals import *
import pygame
from math import sin, cos, radians
from time import asctime

def intl(*args):
    data = []
    for i in args:
        data.append(int(i))
    return tuple(data)

def roundl(*args):
    data = []
    for i in args:
        data.append(round(i))
    return tuple(data)

def amol(lst, **kwargs):
    # Math Operator acting appon All values of a List
    data = list(lst)
    rng = range(2)
    operators = kwargs.keys()
    if 'd' in operators:#divide
        for i in rng:
            data[i] /= kwargs['d']
    return tuple(data)

class Vector2(object):
    def __init__(self, x=0, y=0):
        if str(type(x)) in ("<class 'tuple'>", "<class 'list'>"):
            x, y = x
        self.x = x
        self.y = y
    
    def __repr__(self):
        x, y = self.x, self.y
        return "Vector2(%s, %s)" % (x, y)
    
    #rhs is Right Hand Side
    def __add__(self, rhs):
        return Vector2(self.x + rhs.x, self.y + rhs.y)
    
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    
    def __len__(self):
        return 2
    
    def __iter__(self):
        self.iterc = 0
        return self
    
    def __next__(self):
        if self.iterc <= 1:
            val = [self.x, self.y][self.iterc]
            self.iterc += 1
            return val
        else:
            raise StopIteration
    
    def __getitem__(self, x):
        return [self.x, self.y][x]
    pass

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
    pass

def move_deg(deg, dist, plus=(0, 0)):
    rad = radians(deg)
    plus = Vector2(*plus)
    return roundl( *list( plus + (Vector2(sin(rad), cos(rad)) * dist) ) )

def make_num_sprites():
    middle = Vector2(*amol(SCREENSIZE, d=2))
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
    pygame.init()
    
    screen = pygame.display.set_mode(SCREENSIZE, 0)
    pygame.display.set_caption(NAME)
    
    background = pygame.surface.Surface(SCREENSIZE).convert()
    middle = Vector2(roundl(*amol(SCREENSIZE, d=2)))
    
    Sprite('pic/background.png', amol(SCREENSIZE, d=2), 'Background',
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
        
        display = pygame.surface.Surface(SCREENSIZE).convert()
        
        display.unlock()
        
        screen.fill([255]*3)
        display.blit(background, (0,0))
        
        h, m, s = intl(*' '.join(time.asctime().split('  ')).split(' ')[3].split(':'))
        h %= 12
        h *= 30
        m *= 6
        s *= 6
        #h, m, s = amol([h, m, s], s=180)
        
        hpos = Vector2(move_deg(180-h, 120, middle))
        mpos = Vector2(move_deg(180-m, 160, middle))
        spos = Vector2(move_deg(180-s, 200, middle))
        
        pygame.draw.line(display, (255, 0, 0), middle, spos, 10)
        pygame.draw.line(display, [0]*3, middle, mpos, 10)
        pygame.draw.line(display, [0]*3, middle,hpos, 10)
        
        b = Vector2(1,1)
        pygame.draw.circle(display, (255, 0, 0), spos+b, 5)
        pygame.draw.circle(display, [0]*3, mpos+b, 5)
        pygame.draw.circle(display, [0]*3, hpos+b, 5)
        pygame.draw.circle(display, [2]*3, middle+b, 5)
        
        display.lock()
        
        screen.blit(pygame.transform.flip(display, 1, 0), (0,0))
        
        clock.tick(FPS)
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    run()
