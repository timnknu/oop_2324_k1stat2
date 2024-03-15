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
            pass # тут треба малювати фігуру з допомогою turtle
