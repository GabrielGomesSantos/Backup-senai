# Exercício 5: Classe Cinema
# Crie uma classe chamada Cinema que possua os seguintes atributos:
# nome
# capacidade
# ingressos_vendidos
# A classe também deve ter os seguintes métodos:
# vender_ingressos(quantidade): vende uma certa quantidade de ingressos, diminuindo os lugares disponíveis.
# cancelar_venda(quantidade): cancela a venda e aumenta os lugares disponíveis.
# lugares_disponiveis(): retorna o número de lugares ainda disponíveis.
# Lembre-se de evitar vender mais ingressos do que a capacidade do cinema.


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-Exercicio - 5=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class Cinema:
    def __init__(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade
        self.ingressos_vendidos = 0
    
    def vender_ingressos(self, quantidade):
    
        if (self.ingressos_vendidos + quantidade) <= self.capacidade:
            self.ingressos_vendidos += quantidade
            return True
        
        else:
            print("Não é possível vender essas quantidades de ingressos.")
    
            return False
    
    def cancelar_venda(self, quantidade):
    
        if (self.ingressos_vendidos - quantidade) >= 0:
            self.ingressos_vendidos -= quantidade
            return True
    
        else:
            print("Não há tantos ingressos vendidos para serem cancelados.")
            return False
    
    def lugares_disponiveis(self):
        return self.capacidade - self.ingressos_vendidos
    
cinema1 = Cinema('Cinema ABC', 200)


            
