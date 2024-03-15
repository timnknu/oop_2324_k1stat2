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
    def show(self):
        if not self._visible:
            turtle.penup()
            turtle.goto(self._x, self._y)
            turtle.pendown()
            turtle.color(self._color)
            turtle.circle(100) # тут треба малювати фігуру з допомогою turtle
            self._visible = True
    def hide(self):
        if self._visible:
            turtle.color(turtle.bgcolor())
            turtle.circle(100) # тут треба ще раз малювати фігуру
            self._visible = False
    def move(self, delta_x, delta_y):
        if self._visible:
            self.hide()
            self._x += delta_x
            self._y += delta_y
            self.show()

if __name__ == "__main__":
    #turtle.speed("fastest")
    obj = Figure()
    obj.set_position(50, 50)
    obj.set_color('blue')
    obj.show()
    obj.move(100, 0)
    turtle.exitonclick()