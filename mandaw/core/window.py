from typing import Union
from mandaw.core.color import Color, BasicColors

from sdl2 import SDL_CreateWindow, SDL_GetVideoDriver, SDL_WINDOW_SHOWN


class Window(object):
    def __init__(self, title="Mandaw", width=800, height=600) -> None:
        self.__title: str = title
        self.__width: int = width
        self.__height: int = height
        self.bg_color: Union[Color, BasicColors] = BasicColors.BLACK.value
        self.videoDevice = SDL_GetVideoDriver(0)

    def show(self):
        self.window = SDL_CreateWindow(
            self.__title, 50, 50,
            self.__width, self.__height,
            SDL_WINDOW_SHOWN
        )
    