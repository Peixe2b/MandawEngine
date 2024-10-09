from typing import Any, TypeAlias
from mandaw.interfaces.idevice import IDevice
from sdl2 import SDL_GetMouseState, SDL_BUTTON_LEFT, SDL_BUTTON_RIGHT


BUTTON_RIGHT: TypeAlias = SDL_BUTTON_RIGHT # type: ignore
BUTTON_LEFT: TypeAlias = SDL_BUTTON_LEFT # type: ignore

class Mouse(IDevice):
    def __init__(self) -> None:
        self.x, self.y = 0
        self.press: bool = False
        self.__is_visible = True
        self.__mouse_state: Any = SDL_GetMouseState(None)

    def update(self):
        self.__mouse_state = SDL_GetMouseState(None)
    
    def pressed(self, input):
        return (input in [BUTTON_RIGHT, BUTTON_LEFT])
    
    def get_info(self) -> dict:
        return {
            "cursor_x": self.x, "cursor_y": self.y,
            "mouseState": self.__mouse_state, "isVisible": self.__is_visible
        }
        
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
