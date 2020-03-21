#!/usr/bin/env python3
# Vector2 Class for games

from math import *

__version__ = '0.0.2'
NAME = 'Vector2 Module'

class Vector2(object):
    def __init__(self, x=0, y=0):
        if str(type(x)) in ("<class 'tuple'>", "<class 'list'>"):
            x, y = x
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)
    
    def __repr__(self):
        x, y = self.x, self.y
        return "Vector2(%s, %s)" % (x, y)
    
    @staticmethod
    def from_points(P1, P2):
        P1, P2 = list(P1), list(P2)
        return Vector2(P2[0] - P1[0], P2[1] - P1[1])
    
    def get_magnitude(self):
        return sqrt(self.x**2 + self.y**2)
    
    def get_distance_to(self, point):
        px, py = list(point)
        sx, sy = list(self)
        try:
            px, py, sx, sy = float(px), float(py), float(sx), float(sy)
        except TypeError:
            print(type(point))
            print(list(point))
        return Vector2(px - sx, py - sy).get_magnitude()
    
    def get_normalized(self):
        magnitude = self.get_magnitude()
        if not magnitude == 0:
            x = self.x / magnitude
            y = self.y / magnitude
        else:
            x, y = self.x, self.y
        return Vector2(x, y)
    
    def normalize(self):
        magnitude = self.get_magnitude()
        if not magnitude == 0:
            self.x /= magnitude
            self.y /= magnitude
    
    #rhs is Right Hand Side
    def __add__(self, rhs):
        return Vector2(self.x + rhs.x, self.y + rhs.y)
    
    def __sub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)
    
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        try:
            x, y = self.x / scalar, self.y / scalar
        except ZeroDivisionError:
            x, y = self.x, self.y
        return Vector2(x, y)
    
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
