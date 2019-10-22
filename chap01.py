from turtle import *

def draw(f):
    tracer(0,0)
    f()
    update()

def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)

def triangle(sidelength=100):
    for i in range(3):
        forward(sidelength)
        right(120)



#square()

# exercise 1-2: A CIRCLE OF SQUARES
def circle_square():
    side = 5
    for i in range(60):
        square(side)
        right(5)
        side += 5

def circle_triangle():
    side = 5
    for i in range(60):
        triangle(side)
        right(5)
        side += 5

#draw(circle_square)
draw(circle_triangle)



mainloop()
