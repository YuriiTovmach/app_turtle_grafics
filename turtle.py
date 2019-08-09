import turtle
import random

picture = turtle.Turtle()
turtle.Screen().bgcolor("grey")
colours = ["cyan", "purple", "white", "blue"]
picture.color("cyan")
for i in range(10):
    for i in range(2):
        picture.forward(100)
        picture.right(60)
        picture.forward(100)
        picture.right(120)
    picture.right(36)
    picture.color(random.choice(colours))