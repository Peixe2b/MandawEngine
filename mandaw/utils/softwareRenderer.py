import sdl2


class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window, mandaw):
        self.mandaw = mandaw
        super().__init__(window)

    def render(self, components):
        super().render(components)