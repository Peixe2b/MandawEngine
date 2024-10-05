import sdl2


class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window, mandaw):
        super().__init__(window)
        self.mandaw = mandaw

    def render(self, components):
        sdl2.ext.fill(self.surface, self.mandaw.bg_color)
        super().render(components)