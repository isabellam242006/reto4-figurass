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
                total += item.calcularPrecio() * 0.9  # Apply a 10% discount
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




 