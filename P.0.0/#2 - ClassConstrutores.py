import re 
import os
os.system('cls')

class Pessoas:

    def __init__(self,nome,email,idade):
        if idade <= 0 or idade > 110:
            print("Idade Maluco aqui nao...")
        
        else:        
            self.nome = nome
            self.email = email
            self.idade = idade

    def getNome(self):  return self.nome         
    def getEmail(self):  return self.email         
    def getIdade(self):  return self.idade        

    def setNome(self, novo_Nome):
        self.nome = novo_Nome
             
    def setEmail(self,novo_Email): 
        
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if re.match(padrao, novo_Email): # Boolean 
            self.email = novo_Email
        else:
            return "Email maluco aqui nao..."

    def setIdade(self,nova_Idade):

        if nova_Idade > 0 and nova_Idade < 110:
            self.idade = nova_Idade 
        
        else:      
            return "Idade Maluca aqui nao..."


p = Pessoas("gabriel","g@gmail.com",30)



print(p.getNome())
print(p.getEmail())
print(p.getIdade())

print("Correcao")
p.setNome("gabrielGomes")
p.setEmail("Gomes@gmail.com.br")
p.setIdade(-15)


print(p.getNome())
print(p.getEmail())
print(p.getIdade())
