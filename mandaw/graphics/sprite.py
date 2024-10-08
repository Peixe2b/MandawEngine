from mandaw.utils.game_object import GameObject


class Sprite(GameObject):
    def __init__(self, window, width, height, x, y, color):
        super().__init__(window, width, height, x, y, color)

    def draw(self):
        pass
