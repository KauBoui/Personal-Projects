from turtle import *



# Turtle Constants
Distance = 20
Theta = 60

def draw_path(path):
    for symbol in path:
        if symbol == 'F':
            forward(Distance)
        elif symbol == '-':
            left(Theta)
        elif symbol == '+':
            right(Theta)

axiom = "F-F+F-F"

def productions(axiom):
    production = "F-F+FF-F+F"
    return axiom.replace('F', production)

speed(0)

draw_path(axiom)
productions(axiom)
draw_path(axiom)
productions(axiom)
draw_path(axiom)
productions(axiom)
draw_path(axiom)


exitonclick()
            
