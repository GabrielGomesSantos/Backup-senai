# Exercício 1: Classe Pessoa
# Crie uma classe chamada Pessoa que possua os seguintes atributos:
# nome
# idade
# altura
# A classe também deve ter os seguintes métodos:
# falar(): que imprime "{nome} está falando."
# aniversario(): que aumenta a idade da pessoa em 1.

#=-=-=-=-=-=-=-=-=-=-=-=-=-=- Exercicio - 1 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class Pessoa:
    
    def __init__(self,nome,idade,altura):

        self.nome = nome
        self.idade = idade
        self.altura = altura

    def falar(self): 

        print(self.nome,"Esta falando...")

    def aniversario(self):  
        
        self.idade +=1 
        return self.idade

gabrie = Pessoa("Gabriel",17,1.93)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=