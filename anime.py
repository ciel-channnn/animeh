import turtle

if _name_ =="__main__":

   main()

# Create the screen

wn = turtle.Screen()

wn.title("Character Anime")

wn.bgcolor("lightgreen")

# Create the turtle

tess = turtle.Turtle()

tess.color("blue")

tess.pensize(3)

# Draw the head

tess.penup()

tess.goto(-100, 100)

tess.pendown()

tess.circle(20)

# Draw the eyes

tess.penup()

tess.goto(-120, 105)

tess.pendown()

tess.circle(3)

tess.penup()

tess.goto(-80, 105)

tess.pendown()

tess.circle(3)

# Draw the mouth

tess.penup()

tess.goto(-90, 90)

tess.pendown()

tess.right(45)

tess.forward(15)

tess.left(90)

tess.forward(15)

# Draw the body

tess.penup()

tess.goto(-100, 70)

tess.pendown()

tess.right(90)

tess.forward(50)

# Draw the arms

tess.penup()

tess.goto(-100, 50)

tess.pendown()

tess.right(45)

tess.forward(30)

tess.penup()

tess.goto(-100, 50)

tess.pendown()

tess.left(90)

tess.forward(30)

# Draw the legs

tess.penup()

tess.goto(-90, 0)

tess.pendown()

tess.right(45)

tess.forward(30)

tess.penup()

tess.goto(-90, 0)

tess.pendown()

tess.left(90)

tess.forward(30)

# Hide the turtle

tess.hideturtle()

# Keep the window open

wn.mainloop()
