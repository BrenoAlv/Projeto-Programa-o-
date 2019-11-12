h=float(input("Digite a altura em metros:"))
sexo=input("Digite o sexo: (M/F) ")
peso_m=(72.7*h)-58
peso_f=(62.1*h)-44.7
if sexo=="M":
    print("O peso ideal será de {:.2f} KG.".format(peso_m))
elif sexo=="F":
    print("O peso ideal será de {:.2f} KG.".format(peso_f))
else:
    print("Sexo Inválido.")