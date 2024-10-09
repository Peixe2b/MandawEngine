import os

from typing import Any
from mandaw.core.window_manager import WindowManager


class Mandaw:
    def __init__(self, title="Mandaw", width=800, height=600, flag=0 | 1):
        self.window_manager = WindowManager(title, width, height, flag)
        self.__initialize()
            
    def update(self):
        self.window_manager.game_loop()

    def __initialize(self):
        path: str = os.path.dirname(os.path.abspath(__file__))
        self.icon: str = os.path.join(path, "./assets/mandaw.png")
        self.window_manager.show()
    
    @staticmethod
    def is_running(self) -> bool:
        return self.running

    def get_surface(self) -> Any:
        return self.window_manager.get_surface()
    