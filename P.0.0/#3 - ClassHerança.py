import os 

os.system('cls')

class Veiculo: 
    def __init__(self, marca, modelo):
        self.marca = marca 
        self.modelo = modelo 

    def ligar(self):
        print(f"{self.modelo} está ligado")

    def desligar(self):
        print(f"{self.modelo} está desligado")

class Carro(Veiculo): 
    
    def __init__(self,marca,modelo,numero_de_portas):
        super().__init__(marca, modelo)
        self.numero_de_portas = numero_de_portas
    
    def destrancar(self):   print(f"{self.modelo} está destrancado")

class  Carro_Eltretico(Carro):
        
    def __init__(self, marca, modelo, numero_de_portas, bateria):
        super().__init__(marca, modelo, numero_de_portas)
        self.bateria = bateria
        
    def recarregarBateria(self):
        print(f"{self.modelo} está sem bateria, conect ele ao carregador por 1Hr")

class Moto(Veiculo):
    
    def __init__(self,marca,modelo):
        super().__init__(self,marca,modelo)
    
    def empinar(self):
        print("Randadadan olha a policia")

c1 = Carro_Eltretico("tesla","Model S",4,10000)


c1.destrancar()
c1.recarregarBateria()