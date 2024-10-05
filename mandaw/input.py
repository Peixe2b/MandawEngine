from typing import Union, Any
from mandaw.core.errors import MandawException, MandawSDLError
from sdl2 import SDL_GetKeyboardState, SDL_GetMouseState, SDL_Error

from mandaw.interfaces.idevice import IDevice


all = [
    "Mouse", "Keyboard",
    "Input"
]

class Mouse(IDevice):
    def __init__(self) -> None:
        self.x, self.y = 0
        self.press: bool = False
        self.__mouseState: Any = SDL_GetMouseState(None)

    def set_pos(self, x: int, y: int) -> None:
        pass

    def get_pos(self) -> tuple:
        return (0, 0)

    def get_pressed(self):
        return super().get_pressed()

    def set_visible(self, visible: bool) -> None:
        pass


class Keyboard(IDevice):
    def __init__(self):
        self.__keyboardState: Any = SDL_GetKeyboardState(None)
        self.press: bool = False
        self.release: bool = False
        self.delay: float = 0

    @property
    def GetKeyboardState(self) -> Any:
        return self.__keyboardState 


class Input:
    def __init__(self, device: Union[Mouse, Keyboard]):
        self.__device: Union[IDevice, None] = device

    def get_device(self) -> Union[IDevice, None]:
        return self.__device
