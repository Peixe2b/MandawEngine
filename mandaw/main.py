import os

from typing import Any
from mandaw.core.color import Color
from mandaw.core.window import WindowManager
from mandaw.core.gameTime import GameTime


class Mandaw:
    def __init__(self, title="Mandaw", width=800, height=600, flag=0 | 1):
        self.windowManager = WindowManager(title, width, height, flag)
        self.gameTime = GameTime()
        self.__initialize()
            
    def update(self):
        self.windowManager.gameLoop()
        self.gameTime.updateTime()
        self.world.process()

    def __initialize(self):
        path: str = os.path.dirname(os.path.abspath(__file__))
        self.icon: str = os.path.join(path, "./assets/mandaw.png")
        self.windowManager.show()
    
    @staticmethod
    def isRunning(self) -> bool:
        return self.running
