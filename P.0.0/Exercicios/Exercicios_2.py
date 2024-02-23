# Exercício 2: Classe ContaBancaria
# Crie uma classe chamada ContaBancaria que possua os seguintes atributos:
# titular
# saldo
# A classe também deve ter os seguintes métodos:
# depositar(valor): adiciona o valor ao saldo.
# sacar(valor): subtrai o valor do saldo. Certifique-se de verificar se o saldo é suficiente antes de sacar.

#=-=-=-=-=-=-=-=-=-=-=-=-=-=- Exercicio - 2 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class ContaBancaria:

    def __init__(self, titular, saldo_inicial):

        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):

        if valor >= 0:
            self.saldo +=valor

        else:
            print(f"Irmao se ta bem???? depositar {valor}, seria um saque nao?")

    def sacar(self,valor):

        if self.saldo > valor:
            self.saldo -=valor

        else:
            print("Saldo insuficiente!!")

    def getSaldo(self): return self.saldo
    
gabriel = ContaBancaria("Gabriel",0)

gabriel.depositar(-400)
gabriel.sacar(670)

print(gabriel.getSaldo())

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=