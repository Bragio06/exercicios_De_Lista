lista_Nota = []
lista_Matricula = []

for i in range(5):
    lista_Nota.append(float(input(f"informe a {i+1}° nota :")))
    lista_Matricula.append(int(input(f"informe o {i + 1}° nuemro da matricula: ")))
    print("--------------------------------------------------------------")

print(f"Aqui estão as notas : {lista_Nota}")
media = sum(lista_Nota)/5
print(f"A média é : {media}")

notas_abaixo = 0
notas_acima = 0 

for lista_Nota in lista_Nota :
    if lista_Nota > media:
        notas_acima = notas_acima + 1
       
    if lista_Nota < media :
        notas_abaixo = notas_abaixo + 1
        

print(f"foram acima da media : {notas_acima}")
print(f"as notas abaixo foram : {notas_abaixo}")

