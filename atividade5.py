lista_Elementos = []

for i in range(12): 
    lista_Elementos.append(int(input(f"digite o {i+1}º elemento inteiro")))
    print("--------------------------------------------------------")

print(f"os 12 elementos são :{lista_Elementos}")  
lista_Elementos.sort(reverse=True)
print(f"os elementos invertidos : {lista_Elementos}")