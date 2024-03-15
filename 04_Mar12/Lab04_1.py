import turtle


class Figure:
    def __init__(self):
        self._visible = False
        self._x = 0
        self._y = 0
        self._color = 'green'
    def is_visible(self):
        return self._visible
    def set_color(self, c):
        self._color = c
    def show(self):
        if not self._visible:
            turtle.color(self._color)
            turtle.circle(100) # тут треба малювати фігуру з допомогою turtle
    def hide(self):
        if self._visible:
            turtle.color(turtle.bgcolor())
            turtle.circle(100) # тут треба ще раз малювати фігуру
    def move(self, delta_x, delta_y):
        if self._visible:
            self.hide()
            self._x += delta_x
            self._y += delta_y
            self.show()

if __name__ == "__main__":
    obj = Figure()
    obj.set_color('blue')
    obj.show()
    turtle.exitonclick()