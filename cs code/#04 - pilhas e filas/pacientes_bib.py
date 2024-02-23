import os
fila=[]
i=0

def cls():
   os.system('cls')

def opcoes():
    print("Menu")
    print("1 - Adicionar um paciente")
    print("2 - Mostar a fila de paciente")
    print("3 - Procurar um paciente na fila")
    print("4 - Chamar o proximo paciente")
    
def registro():
    cls()
    global fila
    global i
    i+=1
    nome = input("Nome do paciente:")
    numero = i
    dados={
        "nome": nome,
        "pos": numero,
        "informaçoes": "Passando mal 👍"
    }
    fila.append(dados)
    
def procurar():
    cls()
    global fila
    nome_procurado = input("qual o nome do paciente que você esta prucurando:")
    for dicionario in fila:
        if dicionario['nome'] == nome_procurado:
            print("O paciente", dicionario['nome'],"está na posição", dicionario['pos'])
            break  #usado para sair do loop assim que o item for encontrado
    else:
        print("Nome não encontrado na lista.")
        
def listar():
    cls()
    global fila
    for dicionario in fila:
        nome = dicionario['nome']
        print(nome)

def chamar():
    global fila
    chamar = fila[0]['nome']
    print(chamar,"Doutor esta o chamando na sala 01")
    fila = fila[1:]