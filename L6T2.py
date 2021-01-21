class Road:
    _width = None
    _length = None
    weight = None
    thickness = None


    def __init__(self, w, l):
        self._width = w
        self._length = l

    def square(self):
        self.weight = 25
        self.thickness = 5
        return self._width * self._length * self.weight * self.thickness

a = Road(20, 5000)
print(a.square(), 'kg')