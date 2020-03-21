#!/usr/bin/env python3
# Text like it's in a mirror
# Made by Samuel Davenport

SCREENSIZE = (800, 600)
NAME = 'Mirored Text!'
__version__ = '0.0.1'

FPS = 10
WHITE = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)

import pygame
from pygame.locals import *
from sys import exit

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
    
    screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
    pygame.display.set_caption(NAME)
    
    font = pygame.font.SysFont('Bookman Old Style', 32)
    font_height = font.get_linesize()
    
    display_text = ['Meow!', 'This is text!', 'Backwards!']
    display_text += revlistitems(display_text)
    display_text += display_text#Duplicate
##    cur_item = 0
##    max_items = len(display_text)
    
    clock = pygame.time.Clock()
    
    RUNNING = True
    while RUNNING:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                RUNNING = False
##            if event.type == KEYUP:
##                if event.key == K_UP:
##                    cur_item = (cur_item + 1) % max_items
##                elif event.key == K_DOWN:
##                    cur_item = (cur_item - 1) % max_items
        
        clock.tick(FPS)
        screen.fill(WHITE)
        
        x = SCREENSIZE[0]/2
        y = font_height
        for i in display_text:
            text_surf = font.render( i, True, TEXT_COLOR )
            flipped_surf = pygame.transform.flip(text_surf, 1, 0)
            screen.blit( flipped_surf, (x, y) )
            y += font_height
        
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    run()
