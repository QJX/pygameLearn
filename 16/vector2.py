# -*- coding: utf-8 -*-
import math

class Vector2(tuple):
    def __new__(typ, x=1.0, y=1.0):
        # print(typ, x, y)
        n = tuple.__new__(typ, (int(x), int(y)))
        n.x = x
        n.y = y
        return n

    # def __init__(self, x=1.0, y=1.0):
    #     print(self)

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    def __add__(self, other):
        return self.__new__(type(self), self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return self.__new__(type(self), self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        return self.__new__(type(self), self.x*other, self.y*other)

    def __div__(self, other):
        return self.__new__(type(self), self.x/other, self.y/other)

    def __floordiv__(self, other):
        return self.__new__(type(self), self.x/other, self.y/other)

    def __truediv__(self, other):
        return self.__new__(type(self), self.x/other, self.y/other)

    @staticmethod
    def from_points(P1, P2):
        return Vector2( P2[0] - P1[0], P2[1] - P1[1] )

    def get_magnitude(self):
        return math.sqrt( self.x**2 + self.y**2 )

    def get_length(self):
        return math.sqrt( self.x**2 + self.y**2 )
        
    def normalize(self):
        magnitude = self.get_magnitude()
        if magnitude:
            self.x /= magnitude
            self.y /= magnitude

    def get_normalized(self):
        magnitude = self.get_magnitude()
        x, y = self.x/magnitude, self.y/magnitude
        return self.__new__(type(self), x, y) 

    def get_distance_to(self, other):
        self.from_points(self, other).get_magnitude()
