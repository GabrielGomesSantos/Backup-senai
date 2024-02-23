import math

class FormaGeometrica:

    def area(self):
         raise NotImplementedError("subclasse deve implementar metodo abstrado")

class Retangulo(FormaGeometrica):

    def area(self): return (self.base * self.altura)

class Circulo(FormaGeometrica):

    def area(self): return (math.pi*(self.raio**2))

class Triangulo(FormaGeometrica):

    def area(self): return ((self.base * self.altura)/2)

class Trapezio(FormaGeometrica):

    def area(self): return (((self.baseM + self.basem)*self.altura)/2)

teste = FormaGeometrica()
teste.base = 5
teste.altura = 5


reta = Retangulo()
reta.base = 5
reta.altura = 5

circ = Circulo()
circ.raio = 5

trin = Triangulo()
trin.altura = 5
trin.base = 5


trap = Trapezio()
trap.baseM = 5    
trap.basem = 10
trap.altura = 3

def calcular_area(forma):
    print(f"=========== Exemplo {forma} =========\n")

    print(f"Area: {forma.area()}")



calcular_area(reta)
calcular_area(circ)
calcular_area(trin)
calcular_area(trap)

print(teste.area())










# print("=========== Exemplo Retangulo =========\n")

# print(f"Area: {reta.area()}")

# print("\n=========== Exemplo Circulo ===========\n")

# print(f"Area: {circ.area()}")

# print("\n========== Exemplo triangulo ==========\n")

# print(f"Area: {trin.area()}\n")
