import turtle

# Create screen and turtle object
screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.color("cyan")
pen.pensize(2)
pen.speed(3)

# Draw a square
for _ in range(4):
    pen.forward(100)
    pen.left(90)

# Draw a star
pen.penup()
pen.goto(-150, 0)
pen.pendown()
pen.color("yellow")

for _ in range(5):
    pen.forward(150)
    pen.right(144)

# Keep the window open
screen.mainloop()
