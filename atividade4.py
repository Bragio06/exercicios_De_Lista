lista = []

for i in range(10):
    num = int(input("Insira um número inteiro:"))
    lista.append(num)
    
    valorM = int(input("Insira o valor que você quer achar na sua lista:"))
    position = 0

    if valorM in lista:
        position = lista.index(valorM)
        print(f"A posição do valor que você pediu é: {position}")
    else:
        print("O valor, m, não se encontra na lista")
