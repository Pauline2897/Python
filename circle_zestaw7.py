
#ZADANIE 7.5 KLASA CIRCLE

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.x == other.pt.x and self.y == other.pt.y
        else:
            return self.x == other.x and self.y == other.y


    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return Point(self.x, self.y)

    def __str__(self):
        return str(self.x) + ", " + str(self.y)

PI = 3.14

class Circle:
    #Klasa reprezentująca okręgi na płaszczyźnie.

    def __init__(self, x=0, y=0, radius=1):
        try:
            assert radius > 0
        except AssertionError:
            raise ValueError("promień ujemny")
        self.pt = Point(int(x), int(y))
        self.radius = radius

    def __str__(self):
        return self.pt + "  " + self.radius

    def __repr__(self):
        return "Circle({0}, {1}, {2})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return PI*self.radius**2

    def move(self, x, y):
        return self.pt + Point(x,y)

    def cover(self, other):
        new_radius = (math.sqrt((self.pt.x - other.pt.x)**2
                                + (self.pt.y - other.pt.y)**2) + self.radius + other.radius)/2
        new_x = abs(self.pt.x - other.pt.x)/2
        new_y = abs(self.pt.y - other.pt.y)/2
        return Circle(new_x, new_y, new_radius)
