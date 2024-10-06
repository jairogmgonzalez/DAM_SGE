class Fraccion:
    
    def __init__(self, num, den):
        self.numerador = num
        self.denominador = den
        
        if self.denominador == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        
        # Determina si la fracción es negativa
        if (num * den < 0):
            self.signo = -1
        
        # Simplifica la fracción
        self.simplificarFraccion()

    def simplificarFraccion(self):
        valorMayor = max(abs(self.numerador), abs(self.denominador))
        
        for i in range(2, valorMayor + 1):
            while self.numerador % i == 0 and self.denominador % i == 0:
                self.numerador //= i
                self.denominador //= i


    # Método para sumar dos fracciones
    def __add__(self, fraccionb):
        num = (self.numerador * fraccionb.denominador) + (fraccionb.numerador * self.denominador)
        den = self.denominador * fraccionb.denominador
        
        return Fraccion(num, den)
    

    # Método para comparar dos fracciones (menor que)
    def __lt__(self, fraccionb):
        return self.numerador * fraccionb.denominador < fraccionb.numerador * self.denominador
    

    # Método para comparar dos fracciones (menor o igual que)
    def __le__(self, fraccionb):
        return self.numerador * fraccionb.denominador <= fraccionb.numerador * self.denominador
    

    # Método para comparar dos fracciones (mayor que)
    def __gt__(self, fraccionb):
        return self.numerador * fraccionb.denominador > fraccionb.numerador * self.denominador
    

    # Método para comparar dos fracciones (mayor o igual que)
    def __ge__(self, fraccionb):
        return self.numerador * fraccionb.denominador >= fraccionb.numerador * self.denominador
    

    # Método para comparar dos fracciones (igual que)
    def __eq__(self, fraccionb):
        return (self.numerador == fraccionb.numerador) and (self.denominador == fraccionb.denominador)
    

    def __repr__(self):
        return f"{'-' if self.signo == -1 else ''}{abs(self.numerador)}/{abs(self.denominador)}"
    

# Ejemplo de uso
fraccion1 = Fraccion(1, 2)  # 1/2
fraccion2 = Fraccion(3, 4)  # 3/4
fraccion3 = Fraccion(2, 4)  # 2/4 (que es igual a 1/2)

# Comparaciones
print(fraccion1 < fraccion2)  # True
print(fraccion1 <= fraccion3)  # True
print(fraccion1 > fraccion2)  # False
print(fraccion1 >= fraccion3)  # True
print(fraccion1 == fraccion3)  # True



class FiguraGeometrica:
    
    def superficie (self):
        return 0


import math

class TrianguloRectangulo:
    
    def __init__(self, cateto1, cateto2):
        self.cateto1 = cateto1
        self.cateto2 = cateto2
    
    def calcular_hipotenusa (self):
        return math.hypot(self.cateto1, self.cateto2)
    
    
    def calcular_superficie(self):
        return (self.cateto1 * self.cateto2) / 2


class Rectangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_superficie(self):
        return self.base * self.altura


class listaFiguras:
    
    def __init__(self):
        self.figuras = []
    
    
    def añadir_triangulo(self):
        cateto1 = float(input("Ingrese el primer cateto: "))
        cateto2 = float(input("Ingrese el segundo cateto: "))
        triangulo = TrianguloRectangulo(cateto1, cateto2)
        self.figuras.append(triangulo)
    
    
    def añadir_cuadrado(self):
        lado = float(input("Ingrese el lado del cuadrado: "))
        cuadrado = Rectangulo(lado, lado)
        self.figuras.append(cuadrado)
        
    
    def superficie_total(self):
        superficie_total = 0
        for figura in self.figuras:
            superficie_figura = figura.calcular_superficie()
            superficie_total += superficie_figura

        return superficie_total
    
    
    def total_triangulos(self):
        return sum(1 for figura in self.figuras if isinstance(figura, TrianguloRectangulo))
            
        