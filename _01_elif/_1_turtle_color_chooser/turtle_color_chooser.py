import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    t = turtle.Turtle()

    q = simpledialog.askstring('que','What color pen would you like to draw in: red, blue, green?')
    for i in range(10):
        if q == 'red':
            t.pencolor('red')
        elif q == 'blue':
            t.pencolor('blue')
        elif q == 'green':
            t.pencolor('green')
        else:
            t.pencolor(get_random_color())
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.width(25)
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
