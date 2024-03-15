import turtle


class Figure:
    def __init__(self):
        self._visible = False
        self._x = 0
        self._y = 0
        self._color = 'green'
    def set_position(self, x, y):
        self._x = x
        self._y = y
    def get_position(self):
        return (self._x, self._y)
    def is_visible(self):
        return self._visible
    def set_color(self, c):
        self._color = c
    def _draw(self):
        raise Exception("Not implemented") # "майже абстрактний метод"
    def show(self):
        if not self._visible:
            turtle.color(self._color)
            self._draw() # /!\ намалювати не "коло", а просто "намалювати себе"
            self._visible = True
    def hide(self):
        if self._visible:
            turtle.color(turtle.bgcolor())
            self._draw() # /!\ намалювати не "коло", а просто "намалювати себе"
            self._visible = False
    def move(self, delta_x, delta_y):
        if self._visible:
            self.hide()
            self._x += delta_x
            self._y += delta_y
            self.show()

class Circle(Figure):
    def _draw(self):
        turtle.penup()
        turtle.goto(self._x, self._y)
        turtle.pendown()
        turtle.circle(100)

class Triangle(Figure):
    def _draw(self):
        turtle.penup()
        turtle.goto(self._x, self._y)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(100)
        turtle.setheading(120)
        turtle.forward(100)
        turtle.setheading(240)
        turtle.forward(100)


if __name__ == "__main__":
    turtle.speed("fastest")

    figs = []

    cr = Circle()
    cr.set_position(-50, -100)
    figs.append(cr)

    cr2 = Circle()
    cr2.set_position(-250, -100)
    figs.append(cr2)

    tr = Triangle()
    tr.set_position(0, -150)
    figs.append(tr)

    print(figs)

    for obj in figs:
        obj.show()

    for obj in figs:
        obj.set_color('blue')
        obj.move(100, 0)

    turtle.exitonclick()