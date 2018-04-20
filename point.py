import math


class Point2D:

    """ A point identified by (x, y) coordinates.

    Initialization
    ==============

        Without arguments - create Point2D(0, 0)
        With one argument (only instance of the Point2D) -
            create copy of this instance
        With two arguments (two int or float numbers) -
            create Point2D(x, y)

    Attributes
    ==========

        x - the x-coordinate
        y - the y-coordinate

    Supports
    ========

        Binary operations: +, -, *, **, /, //, %
        Comparison operations: ==, !=
        Unary operations: ~ (inversion), unary -, abs()
        Representation: str()

    Methods
    =======

        coord_items - returns [('x', x), ('y', y)]
        coord_to_list - returns [x, y]
        copy - returns copy of the point
        delta_x - difference between the x-coordinates of two points
        delta_y - difference between the y-coordinates of two points
        distance - distance between two points
        integerize - if x == 1.0 then x = 1, if x == 1.2 then x = 1.2
        line_equation - returns tuple of two coefficients (k, b) of the
            equation 'y = kx + b' of the straight line joining the two points
        midpoint - point that divides the segment in half
        move - x + dx, y + dy (inplace method)
        origin_reflection - reflect point about the origin
        point_reflection - reflect point about the another point
        point_that_div_line - point that divides the segment into
            two segments by the relation
        reflect_x - reflect point about the X-axis
        reflect_y - reflect point about the Y-axis
        rotate_around_origin - rotate point around origin
            by angle in degrees
        rotate_around_point - rotate point around other point
            by angle in degrees
        slope - slope of the segment (by two points)
        slope_from_origin - slope of the segment (one of points is origin)
        quadrant - return one of four numbers of regions that formed
            by dividing the plane by two axes (returns 0 if point lies
            on the axis or on the origin)"""

    def __init__(self, *args):
        q_args = len(args)
        if q_args < 1:
            self.x = 0
            self.y = 0
        elif q_args < 2:
            Point2D.check_obj_type('Point2D', args[0], ('Point2D'))
            self.x = args[0].x
            self.y = args[0].y
        elif q_args == 2:
            for obj in args:
                Point2D.check_obj_type('Point2D', obj, ('int', 'float'))
            self.x = args[0]
            self.y = args[1]
        else:
            msg = 'Point2D() takes 3 positional arguments but {} were given'
            raise TypeError(msg.format(q_args))

    @staticmethod
    def check_obj_type(op, obj, types):
        err_msg = "unsupported operand type(s) for {}: '{}'"
        obj_type = type(obj).__name__
        if obj_type not in types:
            raise TypeError(err_msg.format(op, obj_type))

    def __str__(self):
        return 'Point2D({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        Point2D.check_obj_type('*', other, ('Point2D'))
        x = self.x + other.x
        y = self.y + other.y
        return Point2D(x, y)

    def __sub__(self, other):
        Point2D.check_obj_type('*', other, ('Point2D'))
        x = self.x - other.x
        y = self.y - other.y
        return Point2D(x, y)

    def __mul__(self, number):
        Point2D.check_obj_type('*', number, ('int', 'float'))
        x = self.x * number
        y = self.y * number
        return Point2D(x, y)

    def __rmul__(self, number):
        Point2D.check_obj_type('*', number, ('int', 'float'))
        x = self.x * number
        y = self.y * number
        return Point2D(x, y)

    def __pow__(self, number):
        Point2D.check_obj_type('**', number, ('int', 'float'))
        x = self.x ** number
        y = self.y ** number
        return Point2D(x, y)

    def __truediv__(self, number):
        Point2D.check_obj_type('/', number, ('int', 'float'))
        x = self.x / number
        y = self.y / number
        return Point2D(x, y)

    def __floordiv__(self, number):
        Point2D.check_obj_type('//', number, ('int', 'float'))
        x = self.x // number
        y = self.y // number
        return Point2D(x, y)

    def __mod__(self, number):
        Point2D.check_obj_type('%', number, ('int', 'float'))
        x = self.x % number
        y = self.y % number
        return Point2D(x, y)

    def __abs__(self):
        x = abs(self.x)
        y = abs(self.y)
        return Point2D(x, y)

    def __neg__(self):
        x = -abs(self.x)
        y = -abs(self.y)
        return Point2D(x, y)

    def __invert__(self):
        x = self.x * -1
        y = self.y * -1
        return Point2D(x, y)

    def __eq__(self, other):
        Point2D.check_obj_type('==', other, ('Point2D'))
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        Point2D.check_obj_type('!=', other, ('Point2D'))
        return self.x != other.x and self.y != other.y

    def integerize(self):
        x, y = self.coord_to_list()
        if isinstance(x, float) and x.is_integer():
            x = int(x)
        if isinstance(y, float) and y.is_integer():
            y = int(y)
        return Point2D(x, y)

    def copy(self):
        return Point2D(self)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def quadrant(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
                return 3
        elif self.x > 0 and self.y < 0:
            return 4
        else:
            return 0

    def point_reflection(self, other):
        Point2D.check_obj_type('point_reflection', other, ('Point2D'))
        x = 2 * other.x - self.x
        y = 2 * other.y - self.y
        return Point2D(x, y).integerize()

    def origin_reflection(self):
        return self.__invert__()

    def reflect_x(self):
        return Point2D(self.x, -self.y).integerize()

    def reflect_y(self):
        return Point2D(-self.x, self.y).integerize()

    def rotate_around_point(self, other, degr):
        return (self - other).rotate_around_origin(degr) + other

    def rotate_around_origin(self, degr):
        rad = math.radians(degr)
        sinus = math.sin(rad)
        cosinus = math.cos(rad)
        new_x = round(self.x * cosinus - self.y * sinus, 10)
        new_y = round(self.x * sinus + self.y * cosinus, 10)
        return Point2D(new_x, new_y).integerize()

    def delta_x(self, other):
        Point2D.check_obj_type('delta_x', other, ('Point2D'))
        return abs(self.x - other.x)

    def delta_y(self, other):
        Point2D.check_obj_type('delta_y', other, ('Point2D'))
        return abs(self.y - other.y)

    def distance(self, other):
        return math.sqrt(self.delta_x(other) ** 2 +
                         self.delta_y(other) ** 2)

    def point_that_div_line(self, other, relation):
        """ The method returns the coordinates of the point that
        divides the segment into two segments by the relation
        Example: segment AB (A-----B), relation 3/2 => A---X--B"""
        Point2D.check_obj_type('point_that_div_line', other, ('Point2D'))
        x = (self.x + relation * other.x) / (1 + relation)
        y = (self.y + relation * other.y) / (1 + relation)
        return Point2D(x, y).integerize()

    def midpoint(self, other):
        return self.point_that_div_line(other, 1).integerize()

    def coord_to_list(self):
        return [self.x, self.y]

    def coord_items(self):
        return list(zip('xy', self.coord_to_list()))

    def slope(self, other):
        Point2D.check_obj_type('slope', other, ('Point2D'))
        try:
            return (self.y - other.y) / (self.x - other.x)
        except ZeroDivisionError:
            return math.inf

    def slope_from_origin(self):
        return self.slope(Point2D())

    def line_equation(self, other):
        """The equation of a straight line is 'y = kx + b'
        This method computes the equation of the straight line
        joining the two points and return the two coefficients
        (k, b) as a tuple of two values."""
        k = self.slope(other)
        if k is not math.inf:
            kx = k * self.x
            b = round(self.y - kx, max(len(str(float(kx)).split('.')[1]),
                                       len(str(float(self.y)).split('.')[1])))
            return (k, b)
        return (math.inf, -math.inf)


if __name__ == '__main__':
    # Create points
    A = Point2D(1, 2)
    B = Point2D(-3, 6)
    C = Point2D()
    D = Point2D(1, 12)

    # Clone points
    E = Point2D(A)
    print(E == A)       # True
    print(E is A)       # False
    F = A.copy()
    print(F == A)       # True
    print(F is A)       # False

    # Representation
    print(A)            # Point2D(1, 2)
    print(C)            # Point2D(0, 0)

    # Attributes
    print(A.x)          # 1
    print(B.y)          # 6

    # Quadrants
    print(A.quadrant())                     # 1
    print(B.quadrant())                     # 2
    print(Point2D(-3, -8).quadrant())       # 3
    print(Point2D(6, -5).quadrant())        # 4

    # Coordinates
    print(A.coord_items())                  # [('x', 1), ('y', 2)]
    print(A.coord_to_list())                # [1, 2]

    # Interact with other points
    print(A + B)        # Point2D(-2, 8)
    print(A - B)        # Point2D(4, -4)

    # Interact with numbers
    print(A * 2)        # Point2D(2, 4)
    print(5 * A)        # Point2D(5, 10)
    print(A ** 3)       # Point2D(1, 8)
    print(pow(A, 5))    # Point2D(1, 32)
    print(A / 5)        # Point2D(0.2, 0.4)
    print(B // 2)       # Point2D(-2, 3)
    print(B % 3)        # Point2D(0, 0)

    # Comparisons
    print(A == B)       # False
    print(A == E)       # True
    print(A != E)       # False
    print(A != B)       # True

    # Unary operations
    print(abs(B))       # Point2D(3, 6)
    print(-A)           # Point2D(-1, -2)
    print(~B)           # Point2D(3, -6)

    # Reflection
    print(B.origin_reflection())            # Point2D(3, -6)
    print(A.point_reflection(B))            # Point2D(-7, 10)
    print(A.reflect_x())                    # Point2D(1, -2)
    print(B.reflect_y())                    # Point2D(3, 6)

    # Rotation
    X = Point2D(10, 0)
    M = Point2D(5, 0)
    print(X.rotate_around_point(M, 90))     # Point2D(5, 5)
    print(X.rotate_around_point(M, 180))    # Point2D(0, 0)
    print(X.rotate_around_point(M, 270))    # Point2D(5, -5)
    print(X.rotate_around_point(M, 360))    # Point2D(10, 0)

    print(X.rotate_around_origin(90))       # Point2D(0, 10)
    print(X.rotate_around_origin(180))      # Point2D(-10, 0)
    print(X.rotate_around_origin(270))      # Point2D(0, -10)
    print(X.rotate_around_origin(360))      # Point2D(10, 0)

    # Two points
    print(A.distance(B))                    # 5.656854249492381
    print(A.delta_x(B))                     # 4
    print(A.delta_y(B))                     # 4
    print(A.midpoint(B))                    # Point2D(-1, -1)
    print(A.point_that_div_line(B, 3/2))    # Point2D(-1.4, 4.4)

    # Line properties
    print(A.slope(B))                       # -1.0
    print(A.slope_from_origin())            # 2.0
    print(A.line_equation(D))               # (inf, -inf)
    print(A.line_equation(B))               # (-0.6, 0.8)
