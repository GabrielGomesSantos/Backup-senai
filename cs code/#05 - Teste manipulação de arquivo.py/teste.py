import json
import os 
#Variaveis globais 
i=[]


def clean():
    os.system('cls')

while True:
    clean()
    nome = input("Digite o nome:")
    data = input("Digite a data de aniversario dele:")
    
    dadosn={"nome" : nome,"data" : data}
        
    i = dadosn
    
    with open ("test.json", "a") as file:
        json.dump(i, file, indent=4)
    print("Salvo com sucesso")
