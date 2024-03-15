import turtle

turtle.pendown()

a = 0
n = 10
for i in range(n):
    turtle.setheading(a)
    turtle.forward(100)
    a += 360/n


#turtle.mainloop()
turtle.exitonclick()
