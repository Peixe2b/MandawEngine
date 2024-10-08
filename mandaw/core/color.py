from sdl2 import SDL_Color
from enum import Enum


class Color(SDL_Color):
    def __init__(self, r: int, g: int, b: int, a: int=255):
        super().__init__(
            r, g, b, a
        )


class BasicColors(Enum): # Use ".value" for get color tuple
    BLACK = 0, 0, 0,
    WHITE = 255, 255, 255,
    RED = 255, 0, 0,
    GREEN = 0, 255, 0,
    BLUE = 0, 0, 255,
    CYAN = 0, 255, 255,
    MAGENTA = 255, 0, 255,
    SILVER = 192, 192, 192,
    GRAY = 128, 128, 128,
    PURPLE = 128, 0, 128,
    ORANGE = 255, 165, 0,
    PINK = 255, 192, 203, 
    BROWN = 139, 69, 19,
    SKY = 135, 206, 250
