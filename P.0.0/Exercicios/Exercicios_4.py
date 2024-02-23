# Exercício 4: Classe Carro
# Crie uma classe chamada Carro que possua os seguintes atributos:
# marca
# modelo
# tanque_combustivel (em litros)
# consumo (quantidade de km que o carro percorre por litro)
# A classe também deve ter os seguintes métodos:
# dirigir(distancia): diminui o combustível no tanque com base na distância dirigida e no consumo.
# abastecer(litros): adiciona litros ao tanque. Evite ultrapassar a capacidade do tanque.

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-Exercicio - 4=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class Carro:

    def __init__(self,marca,modelo,tanque_combustivel,consumo):
        self.marca = marca
        self.modelo = modelo 
        self.tanque_combustivel = tanque_combustivel
        self.consumo = consumo

    def dirigir(self,distancia):
        if self.tanque_combustivel >= distancia * self.consumo :
            self.tanque_combustivel -= distancia * self.consumo
        else:
            print("O carro não tem combustível suficiente para essa viagem.")
    
    def abastecer(self,litros):
        if self.tanque_combustivel + litros <= self.capacidade:
            self.tanque_combustivel += litros
        else:
            print("Não é possível abastecer mais combustível neste momento.")


