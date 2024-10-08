from typing import Any
from mandaw.core.color import Color


class GameObject(object):
    def __init__(self, window, width=20, height=20, x=0, y=0, color=Color(255, 255, 255)):
        self.window: Any = window
        self.width: int = width
        self.height: int = height
        self.x: int = x
        self.y: int = y
        self.color: Color = color
    
    def collide(self, other_rect):
        left, top, right, bottom = self.entity.sprite.area
        bleft, btop, bright, bbottom = other_rect.entity.sprite.area
        return(bleft < right and bright > left and btop < bottom and bbottom > top)

    def collidelist(self, other_rect):
        collisions = [True if self.collide(other_rect[i]) else False for i in range(len(other_rect))]
        return any(collisions)

    def center_pos(self):
        self.x = int(self.window.width / 2) - int(self.width / 2)
        self.y = int(self.window.height / 2) - int(self.height / 2)

    def center_x_pos(self):
        self.x = int(self.window.width / 2) - int(self.width / 2)

    def center_y_pos(self):
        self.y = int(self.window.height / 2) - int(self.height / 2)