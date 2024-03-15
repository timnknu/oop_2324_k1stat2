import turtle

turtle.speed("slowest")

turtle.pendown()

a = 0
n = 3
for i in range(n):
    turtle.setheading(a)
    turtle.forward(100)
    a += 360/n
turtle.penup()

turtle.color('red')
turtle.goto(-100, -100)
turtle.pendown()
turtle.goto(-100, -50)
turtle.goto(-50, -50)


#turtle.mainloop()
turtle.exitonclick()
