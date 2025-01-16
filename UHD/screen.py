"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""


from button import Button
class Screen:
    def __init__(self, width: float, height: float, buttons: list[Button]):


        self.__width = width
        self.__height = height

        #Button list
        self.__buttons = buttons


    def draw(self):
        for button in self.__buttons:
            button.draw()




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


    @property
    def buttons(self):
        return self.__buttons

    @buttons.setter
    def buttons(self, value):
        if type(value) != list:
            raise TypeError("attribute buttons must be a list.")
        else:
            for button in value:
                if type(button) != Button:
                    raise TypeError("element from buttons must be a button")
        self.__buttons = value


