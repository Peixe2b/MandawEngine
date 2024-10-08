from time import time
from sdl2 import SDL_GetTicks, SDL_GetPerformanceFrequency


class GameTime:
    def __init__(self):
        self.start, self.__now = time(), SDL_GetTicks()
        self.__last: int = 0
        self.delta_time: int = 0
    
    def update_time(self):
        self.__last, self.__now = self.__now, SDL_GetTicks()
        self.delta_time = int(
            (self.__now - self.__last) * 1000 / SDL_GetPerformanceFrequency()
        )

    def get_last_frame(self) -> int:
        return self.__last
