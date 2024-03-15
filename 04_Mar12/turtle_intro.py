import turtle

turtle.speed("slowest")

turtle.pendown()

a = 0
n = 10

for i in range(n):
    turtle.setheading(a)
    turtle.forward(100)
    a += 360/n

turtle.color(turtle.bgcolor())

for i in range(n):
    turtle.setheading(a)
    turtle.forward(100)
    a += 360/n

turtle.penup()

turtle.color('#CD853F')
turtle.goto(-100, -100)
turtle.pendown()
turtle.goto(-100, -50)
turtle.goto(-50, -50)


#turtle.mainloop()
turtle.exitonclick()
