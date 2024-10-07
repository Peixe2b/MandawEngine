from typing import Union
from mandaw.core.errors import MandawSDLError, MandawException
from mandaw.core.color import Color, BasicColors

from sdl2 import (
    SDL_Init,
    SDL_CreateWindow,
    SDL_GetVideoDriver,
    SDL_WINDOW_SHOWN,
    SDL_DestroyWindow,
    SDL_Quit,
    SDL_Event,
    SDL_PollEvent,
    SDL_QUIT,
    SDL_INIT_VIDEO
)


class Window(object):
    def __init__(self, title=b"Mandaw", width=800, height=600) -> None:
        SDL_Init(SDL_INIT_VIDEO)	
        self.__title = title
        self.__width: int = width
        self.__height: int = height
        self.bg_color: Union[Color, BasicColors] = BasicColors.BLACK.value
        self.window = None

        self.videoDevice = SDL_GetVideoDriver(0)
        if not self.videoDevice:
            raise MandawSDLError("Unable to get video driver")

    def show(self):
        self.window = SDL_CreateWindow(
            self.__title, 50, 50,
            self.__width, self.__height,
            SDL_WINDOW_SHOWN
        )
        if not self.window:
            raise MandawSDLError("Unable to create window")

    def gameLoop(self):
        running = True
        while running:
            event = SDL_Event()
            while SDL_PollEvent(event) != 0:
                if event.type == SDL_QUIT:
                    running = False
        self.cleanup()

    def cleanup(self):
        if self.window:
            SDL_DestroyWindow(self.window)
        SDL_Quit()
    
