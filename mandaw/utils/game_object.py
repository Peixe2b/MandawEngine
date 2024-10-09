from mandaw.core.color import Color
from sdl2 import (
    SDL_Rect,
    SDL_HasIntersection
)

class GameObject(object):
    def __init__(self, width=20, height=20, x=0, y=0, color=Color(255, 255, 255)):
        self.width: int = width
        self.height: int = height
        self.x: int = x
        self.y: int = y
        self.color: Color = color
        self.rect = SDL_Rect(self.x, self.y, self.width, self.height)
    
    def collide(self, other_rect):
        return SDL_HasIntersection(self.rect, other_rect)

    def collidelist(self, other_rects):
        collisions = [self.collide(other_rect) for other_rect in other_rects]
        return any(collisions)
