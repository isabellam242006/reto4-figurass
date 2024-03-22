# reto4-figurass

Para la primera parte de este reto se utilizó el diagrama de clases dado para encontrar las distintas medidas de ciertas figuras que comparten atributos y clases.
La primera parte del código consiste en definir dos clases principales de las cuales se deriva todo. Estas son la case Punto y la clase Línea:
```python
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
```
Luego sigue la clase Shape, la cual contiene todos los atributos y métodos necesarios para cada figura. La clase shape en este caso nos sirve como una especie de plantilla, ya que aquí no se generan las condiciones necesarias para realizar los cálculos pero si se instancian las variables:

```python
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
```
En esta parte se crea la clase Triangle a partir de la clase Shape.
**Para los vértices**: Se le pide al usuario que ingrese las coordenadas de los vértices, y ese hace en el rango de 3 ya que un triángulo tiene 3 vértices. Acá se utiliza la clase Punto para organizar las coordenadas. Por último se agregan a la variable Vertex. Cada vértice se agrega a la lista de vértices.

**Para las aristas**: Se establecen los tres vértices y se calcula el valor de sus distancias a partir de la clase Line

**Para el área**: A partir del algoritmo de Heron que relaciona sus tres aristas para hallar el área

**Para el perímetro**: Se suman todas las aristas contenidas en la lista

**Para los ángulos internos**: Para calcular sus ángulos internos se usó la ley de los cosenos para las tres aristas. Primero se calcula la longitud de sus aristas, posteriormente se utiliza la fórmula y luego se convierte de radianes a grados. Por último se agregan todos estos valores a una lista que los contenga. 

La última parte es crear las subclases de la clase triángulo, las cuales se heredan de él y equivalen a los distintos tipos de triángulo que hay. Agregando además el valor de si son polígonos regulares o irregulares.

```python
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
```
Luego se creó la clase Rectangle la cual usa la misma lógica que la clase Triangle. 
**Para las aristas y los vertices**: Se utilizó la misma lógica para hallar estas variables con la diferencia de que se utilizó en un rango de 4, ya que son 4 vertices y 4 aristas

**Para el área**: Se multiplicaron dos valores de la lista de aristas y así se consiguió el área

**Para el perímetro**: Se sumaron todos los valores de la lista de aristas y así se consiguió el perímetro

**Para los ángulos internos**: Se sabe que todo rectángulo tiene 4 ángulos internos de 90 grados cada uno, así que simplemente se creó una lista con estos valores.

Por último del rectángulo se crea la clase que se hereda la cual es Square, el cuadrado comparte una característica de la clase Rectangle
```python
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
```
```python
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
```
Para la segunda parte del reto, se utilizó el código antes hecho del restaurante y se le hicieron algunas modiificaciones:
**Las modificaciones hechas fueron las siguientes**:
1. Se agregaron setters y getters dentro de las subclases de MenuItem
2. Se editó la parte que calcula el total en la clase Order, añadiendo un descuento del 10% en bebidas
3. Se generó la clase Payment junto con la clases Cash y Card que se heredan de esta. Aquí se tienen en cuenta distintos atributos como el método a pagar, el total a pagar, el valor pagado, el cambio y características propias de la tarjeta como su número, su fecha de vencimiento y su código de seguridad. Además de una función para pagar.
```python
class MenuItem:
    def __init__(self, nombre, precio, impuesto, propina):
        self.precio = precio
        self.impuesto = impuesto
        self.propina = propina
        self.nombre = nombre

    def calcularPrecio(self):
        impuesto = self.precio * self.impuesto
        propina = self.precio * self.propina
        total = self.precio + impuesto + propina
        return total
    
class Entrada(MenuItem):
    def __init__(self, nombre, precio, impuesto, propina, tipo):
        super().__init__(nombre, precio, impuesto, propina)
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo


class Sopa(MenuItem):
    def __init__(self, nombre, precio, impuesto, propina, ingrediente_principal):
        super().__init__(nombre, precio, impuesto, propina)
        self.ingrediente_principal = ingrediente_principal

    def get_ingrediente_principal(self):
        return self.ingrediente_principal

    def set_ingrediente_principal(self, ingrediente_principal):
        self.ingrediente_principal = ingrediente_principal


class Postre(MenuItem):
    def __init__(self, nombre, precio, impuesto, propina, tipo):
        super().__init__(nombre, precio, impuesto, propina)
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo


class Bebida(MenuItem):
    def __init__(self, nombre, precio, impuesto, propina, tipo):
        super().__init__(nombre, precio, impuesto, propina)
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo


class Ensalada(MenuItem):
    def __init__(self, nombre, precio, impuesto, propina, vinagreta):
        super().__init__(nombre, precio, impuesto, propina)
        self.vinagreta = vinagreta

    def get_vinagreta(self):
        return self.vinagreta

    def set_vinagreta(self, vinagreta):
        self.vinagreta = vinagreta


class Pasta(MenuItem):
    def __init__(self, nombre, precio, impuesto, propina, tipo_pasta):
        super().__init__(nombre, precio, impuesto, propina)
        self.tipo_pasta = tipo_pasta

    def get_tipo_pasta(self):
        return self.tipo_pasta

    def set_tipo_pasta(self, tipo_pasta):
        self.tipo_pasta = tipo_pasta

class Order:
    def __init__(self):
        self.items = []
    
    def agregarItem(self, item):   #Esta parte nos permite agregar los items que se deseen
        self.items.append(item)       


    def calcularTotal(self):
        main_course_ordered = any(isinstance(item, Pasta) for item in self.items)
        total = 0
        for item in self.items:
            if isinstance(item, Bebida) and main_course_ordered:
                total += item.calcularPrecio() * 0.9  
            else:
                total += item.calcularPrecio()
        return total

    def imprimirFactura(self):
        for item in self.items:
            print(item.nombre, "- $",item.calcularPrecio())  #Imprime nombre y precio del Item
        print("Total: $",self.calcularTotal())
    
    def aplicarDescuento(self):         #Aplica descuento del 10% con condición
        total = self.calcularTotal()
        if total > 400000:
            for item in self.items:
                item.precio = item.precio * 0.9
    
class Payment:
    def __init__(self, total, method):
        self.total = total
        self.method = method

    def get_total(self):
        return self.total

    def set_total(self, total):
        self.total = total

    def get_method(self):
        return self.method

    def set_method(self, method):
        self.method = method

    def pay(self):
        pass

class Cash(Payment):
    def __init__(self, total, method, cash_received):
        super().__init__(total, method)
        self.cash_received = cash_received

    def get_cash_received(self):
        return self.cash_received

    def set_cash_received(self, cash_received):
        self.cash_received = cash_received

    def pay(self):
        if self.cash_received >= self.total:
            return self.cash_received - self.total
        else:
            return None

class Card(Payment):
    def __init__(self, total, method, card_number, expiration_date, cvv):
        super().__init__(total, method)
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

    def get_card_number(self):
        return self.card_number

    def set_card_number(self, card_number):
        self.card_number = card_number

    def get_expiration_date(self):
        return self.expiration_date

    def set_expiration_date(self, expiration_date):
        self.expiration_date = expiration_date

    def get_cvv(self):
        return self.cvv

    def set_cvv(self, cvv):
        self.cvv = cvv

    def pay(self):
        return True
  

#Creamos el menu con cada item y sus atributos

entrada1 = Entrada("Burrata Figliata", 105000, 0.7, 0.10, "Queso")
entrada2 = Entrada("Berenjenas a la parmesana", 38000, 0.7, 0.10, "Vegetal")
entrada3 = Entrada("Carpaccio de Res", 70000, 0.7, 0.10, "Carne")

pasta1 = Pasta("Pasta Carbonara", 80000, 0.7, 0.10, "Spaghetti")
pasta2 = Pasta("Pasta Pomodoro", 70000, 0.7, 0.10, "Pasta corta")
pasta3 = Pasta("Pasta Putanesca", 75000, 0.7, 0.10, "Spaghetti")
pasta4 = Pasta("Pasta Bolognesa", 85000, 0.7, 0.10, "Fetuccini")
pasta5 = Pasta("Pasta Alfredo", 90000, 0.7, 0.10, "Fetuccini")

postre1 = Postre('Tiramisu de la casa', 22000, 0.7, 0.10, "Tiramisú")
postre2 = Postre("Copa Amaretto", 26000, 0.7, 0.10, "Copa")
postre3 = Postre("Gelato al Pistacchio", 40000, 0.7, 0.10, "Gelatina")
postre4 = Postre("Torta de chocolate", 26000, 0.7, 0.10, "Torta")

bebida1 = Bebida("Bubble Fizz", 50000, 0.7, 0.10, "Licor")
bebida2 = Bebida("Coca Cola", 10000, 0.7, 0.10, 'Refresco')
bebida3 = Bebida("Capuccino", 10000, 0.7, 0.10, "Bebida caliente")
bebida4 = Bebida("Limonada de coco", 14000, 0.7, 0.10, "Limonada")
bebida5 = Bebida("Jugo de Mora", 10000, 0.7, 0.10, "Jugo")

ensalada1 = Ensalada("Insalata Di garedino", 55000, 0.7, 0.10, "Vinagreta Oliva Limón")
ensalada2 = Ensalada("Kale César", 40000, 0.7, 0.10, "Vinagreta tradicional")

sopa1 = Sopa("Sopa Minestrone", 26000, 0.7, 0.10, "Verduras")
sopa2 = Sopa("Sopa Di Pomodoro", 26000, 0.7, 0.10, "Tomates")



# Crea una nueva orden
orden1 = Order()
orden2 = Order()
orden3 = Order()

# Agrega todos los objetos a la orden
orden1.agregarItem(entrada1)
orden1.agregarItem(pasta3)
orden1.agregarItem(postre3)
orden1.agregarItem(bebida4)

orden2.agregarItem(entrada2)
orden2.agregarItem(pasta5)
orden2.agregarItem(postre1)
orden2.agregarItem(sopa1)

orden3.agregarItem(ensalada2)
orden3.agregarItem(pasta2)
orden3.agregarItem(postre2)
orden3.agregarItem(bebida2)

# Imprime el menú con su descuento si existe
print("La factura de la orden 1 es:")
print()


orden1.aplicarDescuento()
orden1.imprimirFactura()
print()
print("La factura de la orden 2 es:")
print()

orden2.aplicarDescuento()
orden2.imprimirFactura()

print()
print("La factura de la orden 3 es:")

orden3.aplicarDescuento()
orden3.imprimirFactura()

metodo = int(input("Elige un método de pago (1 si es con efectivo, 2 si es con tarjeta): "))

if metodo == 1:
    total = orden1.calcularTotal()
    cash_received = float(input("Ingrese el monto: "))
    cash = Cash(total, "Efectivo", cash_received)
    cambio = cash.pay()
    if cambio:
        print("El cambio es de $", cambio)
    else:
        print("El monto recibido no es suficiente")

if metodo == 2:
    total = orden1.calcularTotal()
    card_number = input("Ingrese el número de la tarjeta: ")
    expiration_date = input("Ingrese la fecha de expiración: ")
    cvv = input("Ingrese el código de seguridad: ")
    card = Card(total, "Tarjeta", card_number, expiration_date, cvv)
    if card.pay():
        print("Pago exitoso")
    else:
        print("Pago rechazado")

elif metodo != 1 and metodo != 2:
    print("Método de pago no válido")
```
