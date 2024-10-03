import os
import sdl2, sdl2.ext

from typing import Any, Union
from mandaw.input import Input
from mandaw.color import Color, BasicColors


class Mandaw:
    def __init__(self, title="Mandaw", width=800, height=600, bg_color=Color(0, 0, 0)):
        self.title: str = title
        self.width: int = width
        self.height: int = height
        self.bg_color: Union[Color, BasicColors] = bg_color
        self.running: bool = True
        sdl2.ext.init()

        self.window: Any = sdl2.ext.Window(self.title, size = (self.width, self.height))
        self.window.show()
        self.window.bg_color = bg_color
        
        self.world: Any = sdl2.ext.World()
        self.world.width = self.width
        self.world.height = self.height

        self.__factory: Any = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
        self.world.factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

        self.sprite_renderer: SoftwareRenderer = SoftwareRenderer(self.window, self)
        self.world.add_system(self.sprite_renderer)

        __path: str = os.path.dirname(os.path.abspath(__file__))
        self.icon: str = os.path.join(__path, "./assets/mandaw.png")

        self.input: Input = Input()
        self.now: Any = sdl2.SDL_GetTicks() # private
        self.last: int = 0 # private
        self.dt: int = 0 # private 
        
    def run(self):
        self.__inputs()
        self.__gameTime()
        self.world.process()

    def __gameTime(self):
        self.last, self.now = self.now, sdl2.SDL_GetTicks()
        self.dt = self.__get_dt()

    def __inputs(self):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                quit()
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                    quit()
    
    def __get_dt(self):
        dt = ((self.now - self.last) * 1000 / sdl2.SDL_GetPerformanceFrequency())
        return int(dt)


class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window, mandaw):
        super().__init__(window)
        self.mandaw = mandaw

    def render(self, components):
        sdl2.ext.fill(self.surface, self.mandaw.bg_color)
        super().render(components)
