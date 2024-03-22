import math

class Punto:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def set_x(self, value):
        self._x = value

    def set_y(self, value):
        self._y = value

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


class Line:
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def set_start(self, value):
        self._start = value

    def set_end(self, value):
        self._end = value

    def get_start(self):
        return self._start

    def get_end(self):
        return self._end

    def compute_length(self):
        return math.sqrt((self._end.get_x() - self._start.get_x())**2 + (self._end.get_y() - self._start.get_y())**2)


class Shape:
    def __init__(self, is_regular):
        self._is_regular = is_regular
        self._vertices = []
        self._edges = []

    def set_is_regular(self, is_regular):
        self._is_regular = is_regular
    
    def get_is_regular(self):
        return self._is_regular
    
    def add_vertex(self, vertex):
        self._vertices.append(vertex)
    
    def get_vertices(self):
        return self._vertices.copy()
    
    def add_edge(self, edge):
        self._edges.append(edge)
    
    def get_edges(self):
        return self._edges.copy()

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass


class Triangle(Shape):
    def __init__(self, is_regular):
        super().__init__(is_regular)
        
        for i in range(3):  
            x = float(input(f"Introduce la coordenada x del vértice {i+1}: "))
            y = float(input(f"Introduce la coordenada y del vértice {i+1}: "))
            vertex = Punto(x, y)
            self.add_vertex(vertex)
        
        for i in range(3):  
            start = self._vertices[i]
            end = self._vertices[(i+1)%3]
            edge = Line(start, end)
            self.add_edge(edge)
        
    def compute_area(self):
        a = self._edges[0].compute_length()
        b = self._edges[1].compute_length()
        c = self._edges[2].compute_length()
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    
    def compute_perimeter(self):
        perimeter = sum(edge.compute_length() for edge in self._edges)
        return perimeter

    def compute_inner_angles(self):
        angles = []
        for i in range(3):
            a = self._edges[i].compute_length()
            b = self._edges[(i+1)%3].compute_length()
            c = self._edges[(i+2)%3].compute_length()
            angle = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
            angles.append(angle)
        return angles


class Isosceles(Triangle):
    def __init__(self):
        super().__init__(False)


class Equilateral(Triangle):
    def __init__(self):
        super().__init__(True)


class Scalene(Triangle):
    def __init__(self):
        super().__init__(False)


class TriRectangle(Triangle):
    def __init__(self):
        super().__init__(False)

class Rectangle(Shape):
    def __init__(self, is_regular):
        super().__init__(is_regular)
        
        for i in range(4):  
            x = float(input(f"Introduce la coordenada x del vértice {i+1}: "))
            y = float(input(f"Introduce la coordenada y del vértice {i+1}: "))
            vertex = Punto(x, y)
            self.add_vertex(vertex)
        
        for i in range(4):  
            start = self._vertices[i]
            end = self._vertices[(i+1)%4]
            edge = Line(start, end)
            self.add_edge(edge)
        
    def compute_area(self):
        a = self._edges[0].compute_length()
        b = self._edges[1].compute_length()
        area = a * b
        return area
    
    def compute_perimeter(self):
        perimeter = sum(edge.compute_length() for edge in self._edges)
        return perimeter

    def compute_inner_angles(self):
        angles = [90, 90, 90, 90]
        return angles


class Square(Rectangle):
    def __init__(self):
        super().__init__(True)

#Imprimir los resultados

triangle = Triangle(False)
area = triangle.compute_area()
print("El área del triángulo es:", area)

perimeter = triangle.compute_perimeter()
print("El perímetro del triángulo es:", perimeter)

if triangle.get_is_regular():
    print("El triángulo es regular")
else:
    print("El triángulo no es regular")

angles = triangle.compute_inner_angles()
print("Los ángulos internos del triángulo son:", angles)

lengths = [edge.compute_length() for edge in triangle.get_edges()]

if len(set(lengths)) == 1:
    print("Type: Equilateral")
elif len(set(lengths)) == 2:
    print("Type: Isosceles")
else:
    print("Type: Scalene")


rectangle = Rectangle(False)

area = rectangle.compute_area()
print("El área del rectángulo es:", area)

perimeter = rectangle.compute_perimeter()
print("El perímetro del rectángulo es:", perimeter)

angles = rectangle.compute_inner_angles()
print("Los ángulos internos del rectángulo son:", angles)

