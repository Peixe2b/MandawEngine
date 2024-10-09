from typing import Union

from mandaw.core.vector import Vector2
from mandaw.core.rectangle import Rectangle

from sdl2 import (
    SDL_LoadBMP,
    SDL_BlitSurface
)


class TextureBMP:
    """
    A simple image
    """

    def __init__(self, filename: str, position: Union[Vector2, Rectangle]):
        self.filename = filename
        self.pos = [position.x, position.y]
        self.image = SDL_LoadBMP(filename)
    
    def blit(self, surface):
        SDL_BlitSurface(
            self.image, Rectangle(self.pos[0], self.pos[1]),
            surface, None
        )