from typing import Any, Union

from mandaw.core.errors import MandawSDLError
from mandaw.core.gametime import GameTime
from mandaw.core.color import Color, BasicColors

from sdl2 import (
    SDL_Init,
    SDL_WasInit,
    SDL_CreateWindow,
    SDL_GetVideoDriver,
    SDL_DestroyWindow,
    SDL_Quit,
    SDL_Event,
    SDL_PollEvent,
    SDL_GetWindowSurface,
    SDL_UpdateWindowSurface,
    SDL_QUIT,
    SDL_INIT_VIDEO,
    SDL_WINDOWPOS_CENTERED,
    SDL_WINDOW_SHOWN,
    SDL_WINDOW_OPENGL
)


class WindowManager(object):
    def __init__(self, title=b"Mandaw", width=800, height=600, flag: int=0 | 1) -> None:
        SDL_Init(SDL_INIT_VIDEO)
        self.__title = title.encode()
        self.__width: int = width
        self.__height: int = height
        self.__flag = flag
        self.bg_color: Union[Color, BasicColors] = BasicColors.BLACK.value
        self.window = None
        self.game_time = GameTime()
        self.running: bool = True
        self.video_device = SDL_GetVideoDriver(0)
        self.__surface = SDL_GetWindowSurface(self.window)

        if not self.video_device:
            raise MandawSDLError("Unable to get video driver")

    def show(self):
        self.window = SDL_CreateWindow(
            self.__title, SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
            self.__width, self.__height,
            self.get_window_mode()
        )
        if not self.window:
            raise MandawSDLError("Unable to create window")

    def game_loop(self):
        while self.running:
            self.game_time.update_time()
            event = SDL_Event()
            while SDL_PollEvent(event) != 0:
                if event.type == SDL_QUIT:
                    self.running = False
            SDL_UpdateWindowSurface(self.__surface)
        self.cleanup()

    def get_window_mode(self) -> Any:
        if self.__flag == 0:
            return SDL_WINDOW_SHOWN
        return SDL_WINDOW_OPENGL    

    def cleanup(self):
        if SDL_WasInit(SDL_INIT_VIDEO):
            SDL_DestroyWindow(self.window)
        SDL_Quit()

    @property
    def get_surface(self) -> Any:
        return self.__surface
