lista=[]
for i in range(4):
    lista.append(int(input(f"digite o {i + 1}º numero inteiro ")))

print(lista)  
maior_elemento = lista[0]
indice_maior = 0

for i in range(1,len(lista)):
    if lista[i] > maior_elemento :
        indice_maior = i
