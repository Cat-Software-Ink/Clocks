#!/usr/bin/env python3
# Pygame Clock simplified
# Created by Samuel Davenport

NAME = 'Clock'
__version__ = '0.0.4'

SCREENSIZE = (800, 600)
FPS = 2

from math import sin, cos, radians
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
            input('Press Return to continue. ')
    if answer.lower() == 'n':
        print('To manually install Pygame, go to your system command prompt and type in the command \'pip3 install Pygame\'.')
        input('Press Return to continue. ')
    abort()

def intl(*args):
    # Convert any list's values into intigers
    data = []
    for i in args:
        data.append(int(i))
    return tuple(data)

def roundl(*args):
    # Round any list's values
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
    # 2D Vector Class
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
    # Sprite class
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
    # Do the triganometry to move a distance an angle, added to a given value (defaults to 0, 0)
    rad = radians(deg)
    plus = Vector2(*plus)
    return roundl( *list( plus + (Vector2(sin(rad), cos(rad)) * dist) ) )

def make_num_sprites():
    # Make the number sprites
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
    pygame.init() # Initiate Pygame
    
    # Set up the window
    screen = pygame.display.set_mode(SCREENSIZE, 0)
    pygame.display.set_caption(NAME)
    
    # Make a blank surface to store stuff temporarly
    background = pygame.surface.Surface(SCREENSIZE).convert()
    middle = Vector2(roundl(*amol(SCREENSIZE, d=2)))
    
    background.fill([255, 0, 0]) # Make the background red
    pygame.draw.circle(background, [0]*3,   middle, 260)# Make the black circle for the clock in the middle
    pygame.draw.circle(background, [255]*3, middle, 230)# Make the smaller white circle for the clock in the middle
    
    # Make the numbers be in our background
    for sprite in make_num_sprites():
        sprite.render(background)
    
    RUNNING = True
    
    # Initialize FPS clock
    clock = pygame.time.Clock()
    
    while RUNNING:
        # Event handler so if we call a quit, we quit
        for event in pygame.event.get():
            if event.type == QUIT:
                RUNNING = False
        
        # Prepare screen for modification
        screen.unlock()
        
        # Fill the screen white
        screen.fill([255]*3)
        
        # Put oir base clock image on the screen
        screen.blit(background, (0, 0))
        
        # Get the current system time
        h, m, s = intl(*' '.join(asctime().split('  ')).split(' ')[3].split(':'))
        
        # Make 12 hour time
        h %= 12
        
        # Make the times fractions of 360; Hours = hours * 30, mins = mins * 6, secs = secs * 6
        h *= 30
        m *= 6
        s *= 6
        
        # Get the hands to be like a realistic clock, and not jerky
        m += ((s / 360) * 6)
        h += ((m / 360) * 30)
        
        # Get the position each hand needs to end at
        hpos = Vector2(move_deg(180-h, 120, middle))#hour
        mpos = Vector2(move_deg(180-m, 160, middle))#min
        spos = Vector2(move_deg(180-s, 200, middle))#sec
        
        # Draw the hands
        pygame.draw.line(screen, (255, 0, 0), middle, spos, 10)#sec
        pygame.draw.line(screen, [0]*3, middle, mpos, 10)#min
        pygame.draw.line(screen, [0]*3, middle,hpos, 10)#hour
        
        # Draw circles for the hands so they look fancy instead of jagged edges
        b = Vector2(1, 1)#Get how much offset from the end the circles should be
        pygame.draw.circle(screen, (255, 0, 0), spos+b, 5)#sec hand
        pygame.draw.circle(screen, [0]*3, mpos+b, 5)#min hand
        pygame.draw.circle(screen, [0]*3, hpos+b, 5)#hour hand
        pygame.draw.circle(screen, [2]*3, middle+b, 5)#center
        
        screen.lock()# Lock screen for updating the display
        
        clock.tick(FPS)# Tick the FPS clock
        pygame.display.update()# Update the window
    pygame.quit()# When we done running, quit and close the window

if __name__ == '__main__':
    # If we're not imported as a module, do everything
    run()
