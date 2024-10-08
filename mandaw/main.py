import os

from mandaw.core.window_manager import WindowManager
from mandaw.core.gametime import GameTime


class Mandaw:
    def __init__(self, title="Mandaw", width=800, height=600, flag=0 | 1):
        self.window_manager = WindowManager(title, width, height, flag)
        self.gameTime = GameTime()
        self.__initialize()
            
    def update(self):
        self.window_manager.game_loop()
        self.gameTime.updateTime()

    def __initialize(self):
        path: str = os.path.dirname(os.path.abspath(__file__))
        self.icon: str = os.path.join(path, "./assets/mandaw.png")
        self.window_manager.show()
    
    @staticmethod
    def isRunning(self) -> bool:
        return self.running
