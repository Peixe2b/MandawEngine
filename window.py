from mandaw import *

game = Mandaw("Mandaw", 800, 600)

square = GameObject(game, width = 20, height = 20, color = Color(255, 0, 0))
square.center()

color1 = Color(32, 19, 200)
color2 = BasicColors.RED

while True:
    square.draw()
    game.run()