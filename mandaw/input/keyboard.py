from typing import Any
from mandaw.interfaces.idevice import IDevice
from sdl2 import SDL_GetKeyboardState


class Keyboard(IDevice):
    def __init__(self):
        self.__keyboardState: Any = SDL_GetKeyboardState(None)
        self.press: bool = False
        self.release: bool = False
        self.delay: float = 0

    @property
    def get_keyboard_state(self) -> Any:
        return self.__keyboardState 
