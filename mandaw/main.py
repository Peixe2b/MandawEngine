import os
import sdl2, sdl2.ext

from typing import Any, Union
from mandaw.input import Input
from mandaw.color import Color, BasicColors


__all__ = [
    "Mandaw"
]

class Mandaw:
    def __init__(self, title="Mandaw", width=800, height=600, bg_color=Color(0, 0, 0)):
        sdl2.ext.init()
        self.title: str = title
        self.width: int = width
        self.height: int = height
        self.bg_color: Union[Color, BasicColors] = bg_color
        self.running: bool = True
        
        self.world: Any = sdl2.ext.World()
        self.window: Any = sdl2.ext.Window(self.title, size = (self.width, self.height))        
        self.__factory: Any = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
        self.world.factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

        self.__initialize()
        self.sprite_renderer: SoftwareRenderer = SoftwareRenderer(self.window, self)
        self.world.add_system(self.sprite_renderer)

        self.input: Input = Input()
        self.__now: Any = sdl2.SDL_GetTicks()
        self.__last: int = 0
        self.__dt: int = 0 
    
    def __initialize(self): # Initalize all configurations 
        self.window.bg_color = self.bg_color
        self.world.width = self.width
        self.world.height = self.height
        # Set icon
        __path: str = os.path.dirname(os.path.abspath(__file__))
        self.icon: str = os.path.join(__path, "./assets/mandaw.png")
        
        # Show window
        self.window.show()

    def run(self):
        self.__inputs()
        self.__gameTime()
        self.world.process()

    def __gameTime(self):
        self.__last, self.__now = self.__now, sdl2.SDL_GetTicks()
        self.__dt = self.__get_dt()

    def __inputs(self):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                quit()
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                    quit()
    
    def __get_dt(self):
        dt = ((self.__now - self.__last) * 1000 / sdl2.SDL_GetPerformanceFrequency())
        return int(dt)


class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window, mandaw):
        super().__init__(window)
        self.mandaw = mandaw

    def render(self, components):
        sdl2.ext.fill(self.surface, self.mandaw.bg_color)
        super().render(components)
