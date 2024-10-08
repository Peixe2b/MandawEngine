from typing import Any
from mandaw.interfaces.idevice import IDevice
from sdl2 import SDL_GetMouseState


class Mouse(IDevice):
    def __init__(self) -> None:
        self.x, self.y = 0
        self.press: bool = False
        self.__is_visible = True
        self.__mouse_state: Any = SDL_GetMouseState(None)

    def initialize(self):
        pass
    
    def pressed(self):
        return super().pressed()

    def get_info(self) -> dict:
        return {
            "cursor_x": self.x, "cursor_y": self.y,
            "mouseState": self.__mouse_state, "isVisible": self.__is_visible
        }
    
    def disconnect(self):
        return super().disconnect()
    
    def set_pos(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def set_visible(self, visible: bool) -> None:
        self.__is_visible = visible

    def get_pos(self) -> tuple:
        return (self.x, self.y)

    @property
    def get_mouse_state(self) -> Any:
        return self.__mouse_state
