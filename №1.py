import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def length(self, other):
        distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return round(distance, 2)
class PatchedPoint(Point):
    def __init__(self, *parameters):
        if not parameters:
            super().__init__(0, 0)
        elif len(parameters) == 1:
            super().__init__(parameters[0][0], parameters[0][1])
        elif len(parameters) == 2:
            super().__init__(parameters[0], parameters[1])

point = PatchedPoint()
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)