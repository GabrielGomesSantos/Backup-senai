import json 

lista = []


with open ("test.json", "r") as file:
    lista.append(json.load(file))
    
# Inicialize listas vazias para cada chave
nomes = []
datas = []

# Percorra a lista e separe os itens pelas chaves
for item in lista:
    if 'nome' in item:
        nomes.append(item['nome'])
    if 'data' in item:
        datas.append(item['data'])

# Imprima as listas separadas
print("Nomes:", nomes)
print("Datas:", datas)
    