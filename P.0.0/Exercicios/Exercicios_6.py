# Implemente a classe Funcionario
# Atributos: nome, salario 
# métodos: addAumento (valor) ; ganhoAnual() ; exibeDados() - imprime os valores do funcionário.

# a) crie a classe Assistente, que também é um funcionário, e que possui um número de matricula 
# (faça os métodos GET e SET). Sobrescreva a método exibeDados().

# b) sabendo que os Assistentes Técnicos possuem um bonus salarial  (500)
# e que os Assistentes Administrativos possuem um turno (dia ou noite) e um adicional noturno, crie as classes Tecnico e Administrativo e 

#sobrescreva:  o método ganhoAnual() de ambas as classes (Administrativo e Tecnico)

class Funcionario:

    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

    def addAumento(self,valor):
        self.salario +=valor
        return f"salario de {self.nome} agora é de {self.salario}"
    
    def ganhoAnual(self):
        salario_anual = self.salario * 12
        return salario_anual
        
    
    def exibeDados(self):
        print("========== Dados Principais ==========\n")
        print(f"Funcionario: {self.nome}\nSalario base: {self.salario}")

class Assistente(Funcionario):
    
    def __init__(self, nome, salario, matricula):
        super().__init__(nome, salario)
        self.numero_de_matricula = matricula
    
    def exibeDados(self):
        super().exibeDados()
        print(f"N° matrícula: {self.numero_de_matricula}")

    def setMatricula(self,matricula_nova):
        self.numero_de_matricula = matricula_nova

class Assistente_Tecnico(Assistente):

    def __init__(self, nome, salario, matricula):
        super().__init__(nome, salario, matricula)
        self.bonus = 500

    def ganhoAnual(self):
        salario = super().ganhoAnual()
        salario += (self.bonus*12)
        return salario

    def exibeDados(self):
        super().exibeDados()
        print("Cargo: Assistente Técnico")
        print(f"Salario Anual: {self.ganhoAnual()}")

class Assistente_Administrativo(Assistente):

    def __init__(self, nome, salario, matricula, turno):
        super().__init__(nome, salario, matricula)
        self.turno = turno
        self.adicional_noturno = 200 if turno == "noite" else 0

    def ganhoAnual(self):
        salario_anual = super().ganhoAnual()
        salario_anual += self.adicional_noturno
        return salario_anual

    def exibeDados(self):
        super().exibeDados()
        print("Cargo: Assistente Administrativo")
        print(f"Turno: {self.turno}")
        print(f"Salario Anual: {self.ganhoAnual()}")

# Cenário de teste funcionário e métodos
# f1 = Funcionario("Fernanda", 100)
# f1.exibe_dados()
# print("---------------------------")
# f1.addAumento(300)
# print("---------------------------")
# f1.ganhoAnual()
# print("---------------------------")

# # Cenário de teste Assistente
# a1= Assistente("Gomes", 50, "A123")
# a1.exibe_dados()
# a1.set_nova_matricula("A111")
# print("---------------------------")

# Cenário de teste técnico 
tec1 = Assistente_Tecnico("Fe",1000,"T9595")
tec1.ganhoAnual()
print("---------------------------")
tec1.exibeDados()
print("---------------------------")

# Cenário de teste adm
# adm1 = Administrativo("Scaratinho",100,"A256", "2")
# adm1.ganhoAnual()
# print("---------------------------")
# adm1.exibe_dados()