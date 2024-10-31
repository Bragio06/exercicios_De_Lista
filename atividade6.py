lista_elemento = []
for i in range(12):
    lista_elemento.append(int(input(f"digite o {i + 1}º numero :")))

x = int((input("digite a posição   de X :")))
y = int(input("digite a posição de Y :"))
posição1 = lista_elemento.index(x)
posição2 = lista_elemento.index(y)
soma = posição1 + posição2
print(soma)
