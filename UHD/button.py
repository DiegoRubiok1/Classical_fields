"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""
import pyxel
from pyxel.pyxel_wrapper import MOUSE_BUTTON_LEFT

def bltp(x, y, img, u, v, w, h, scale, colkey=None):
    scale = int(scale)
    for i in range(w * scale):  # Ancho escalado
        for j in range(h * scale):  # Alto escalado
            # Dibuja píxel a píxel ampliado
            pyxel.blt(x + i, y + j, img, u + i // scale, v + j // scale, 1, 1, colkey)

class Button:
    def __init__(self, x: int, y: int, width: float, height: float,
                 text: str):

        #Position
        self.__x = x
        self.__y = y

        # Height and width
        self.__width = width
        self.__height = height

        # Text
        self.text = str(text)
        self.__char_tuple = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S',  'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ')
        self.__num_tuple = ('0','1','2','3','4','5','6','7','8','9')

    def btnp(self, x: float, y: float) -> bool:
        cursor_in_button = (self.__x < x < self.__x + self.__width and
                            self.__y < y < self.__y + self.__height)
        if cursor_in_button and pyxel.btnp(MOUSE_BUTTON_LEFT):
            print("Button pressed")
            return True

    def draw(self):
        # Draws the rectangle
        pyxel.rect(self.__x, self.__y, self.__width, self.__height, 3)

        #Draw the text
        i = 0
        scale = self.__height // 8
        for char in self.text:
            for j in range(len(self.__char_tuple)):
                if self.__char_tuple[j] == char:
                    bltp(self.__x + self.__width//15 + i * 8 *scale,
                         self.__y + scale*  self.__height//15 +scale, 0, j*8,
                         0, 8,
                         8, scale)
            i += 1