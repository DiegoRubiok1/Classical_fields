"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""
from logging import raiseExceptions

import pyxel
class Screen:
    def __init__(self, width: float, height: float, buttons):
        self.__width = width
        self.__height = height

        #parámetros pyxel





    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) and value > 0:
            self.__width = value

        else:
            raise Exception("Parameter: width not valid. Must be "
                            "positive integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) and value > 0:
            self.__height = value
        else:
            raise Exception("Parameter: height not valid. Must be "
                            "positive integer")


