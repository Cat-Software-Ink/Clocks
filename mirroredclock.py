#!/usr/bin/env python3
# Clock numbers like it's in a mirror
# Made by Samuel Davenport
# Requested by Anthony Williams

SCREENSIZE = (25, 75)
NAME = 'Clock'
__version__ = '0.0.1'

FPS = 10
WHITE = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)

import pygame
from pygame.locals import *
import time

def _int(*args):
    data = []
    for i in args:
        data.append(int(i))
    return tuple(data)

def _float(*args):
    data = []
    for i in args:
        data.append(float(i))
    return tuple(data)

def _amol(lst, **kwargs):
    # Math Operator acting appon All values of a List
    data = list(lst)
    rng = range(len(data))
    operators = kwargs.keys()
    if 'a' in operators:#add
        for i in rng:
            data[i] += kwargs['a']
    if 's' in operators:#subtract
        for i in rng:
            data[i] -= kwargs['s']
    if 'm' in operators:#multiply
        for i in rng:
            data[i] *= kwargs['m']
    if 'd' in operators:#divide
        for i in rng:
            data[i] /= kwargs['d']
    if 'p' in operators:#power
        for i in rng:
            data[i] **= kwargs['p']
    return tuple(data)

def rev(text):
    # Reverse text
    v = list(text)
    v.reverse()
    return ''.join(v)

def revlistitems(_list):
    # Reverse the items of a list
    data = []
    for i in _list:
        data.append(rev(str(i)))
    return data

def run():
    pygame.init()
    
    font = pygame.font.SysFont('Bookman Old Style', 32)
    font_height = font.get_linesize()
    
    SCREENSIZE = (round(font_height*2), round(font_height*3))
    SCREENSIZE = _amol(SCREENSIZE, m=2)
    
    screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
    pygame.display.set_caption(NAME) 
    
    display_text = ''
    
    clock = pygame.time.Clock()
    
    RUNNING = True
    while RUNNING:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                RUNNING = False
        
        clock.tick(FPS)
        display_text = time.asctime().split(' ')[3].split(':')
        screen.fill(WHITE)
        
        x = SCREENSIZE[0]/2-(font_height/2)
        y = SCREENSIZE[1]/2-font_height
        for i in display_text:
            text_surf = font.render( i, True, TEXT_COLOR )
            flipped_surf = pygame.transform.flip(text_surf, 1, 0)
            screen.blit( flipped_surf, (x, y) )
            y += font_height
        
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    run()
