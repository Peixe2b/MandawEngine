from mandaw import *


game = Mandaw("Game1")

square = GameObject(game)
square.center_pos()


while True:
    square.draw()
    game.update()
