lista_idade=[]
for i in range(4):
    lista_idade.append(f"qual a idade do { i + 1}º aluno:")

print(lista_idade)

maior_que_13 = 0
menor_que_13 = 0

for idade in lista_idade :
    if idade > 13 :
        maior_que_13 = maior_que_13 + 1
    if idade < 13 :
        menor_que_13 = menor_que_13 + 1

print(maior_que_13)
print(menor_que_13) 