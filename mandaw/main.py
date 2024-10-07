import os
import sdl2, sdl2.ext

from typing import Any
from mandaw.core.color import Color
from mandaw.core.window import Window
from mandaw.core.gameTime import GameTime
from mandaw.utils.softwareRenderer import SoftwareRenderer


class Mandaw:
    def __init__(self, title="Mandaw", width=800, height=600):
        self.window = Window(title, width, height)
        self.gameTime = GameTime()
        self.running: bool = True
        self.__initialize()
            
    def update(self):
        self.window.gameLoop()
        self.gameTime.updateTime()
        self.world.process()

    def set_background_color(self, color: Color):
        self.window.bg_color = color

    def __initialize(self):
        __path: str = os.path.dirname(os.path.abspath(__file__))
        self.icon: str = os.path.join(__path, "./assets/mandaw.png")
        self.window.show()
