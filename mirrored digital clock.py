#!/usr/bin/env python3
# Clock numbers like it's in a mirror
# Made by Samuel Davenport

SCREENSIZE = (25, 75)
NAME = 'Clock'
__version__ = '0.0.2'

FPS = 2
WHITE = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)

from time import asctime
from os import sys, system, abort
try:
    from pygame.locals import *
    import pygame
except ImportError:# If pygame is not installed, help the user install it.
    print('Error: Pygame Module is not installed!', file=sys.stderr)
    while True:
        answer = input('Would you like to automatically install Pygame? (y/n) : ')
        if answer.lower() in ('y', 'n'):
            break
        else:
            print('Please type a valid response')
    if answer.lower() == 'y':
        print('Attemting to install Pygame...')
        resp = system('pip3 install Pygame')
        if str(resp) != '0':
            print('Something went wrong installing Pygame.')
            answer = 'n'
        else:
            print('Pygame installed successfully! Please restart the program.')
            input('Press Return to Continue. ')
    if answer.lower() == 'n':
        print('To manually install Pygame, go to your system command prompt and type in the command \'pip3 install Pygame\'.')
        input('Press Return to continue. ')
    abort()

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
        display_text = ' '.join(asctime().split('  ')).split(' ')[3].split(':')
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
