import os
import sdl2, sdl2.ext

from typing import Any, Union
from mandaw.core.gameTime import GameTime
from mandaw.core.color import Color, BasicColors
from mandaw.utils.softwareRenderer import SoftwareRenderer


class Mandaw:
    def __init__(self, title="Mandaw", width=800, height=600, bg_color=Color(0, 0, 0)):
        sdl2.ext.init()
        self.title: str = title
        self.width: int = width
        self.height: int = height
        self.bg_color: Union[Color, BasicColors] = bg_color
        self.running: bool = True
        
        self.world: Any = sdl2.ext.World()
        self.window: Any = sdl2.ext.Window(self.title, size=(self.width, self.height))        
        self.world.factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

        self.__initialize()
        self.sprite_renderer: SoftwareRenderer = SoftwareRenderer(self.window, self)
        self.world.add_system(self.sprite_renderer)
        self.gameTime = GameTime()
    
    def update(self):
        self.__inputs()
        self.gameTime.updateTime()
        self.world.process()

    def __initialize(self): # Initalize all configurations 
        self.window.bg_color = self.bg_color
        self.world.width = self.width
        self.world.height = self.height
        # Set icon
        __path: str = os.path.dirname(os.path.abspath(__file__))
        self.icon: str = os.path.join(__path, "./assets/mandaw.png")
        
        # Show window
        self.window.show()

    def __inputs(self):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                quit()
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                    quit()
