sal_b = float(input("Digite o seu salário bruto: "))
sexo = input("Digite o sexo: ")
desc1 = sal_b*5/100
sal_liq1 = sal_b - desc1
desc2= sal_b*3/100
sal_liq2= sal_b-desc2
if sexo == "M" or sexo == 'm':
    print("O desconto de 5% do salário bruto será de R${:.2f} e o salário líquido será de R${:.2f}.".format(desc1,sal_liq1))
else:
    print("O desconto de 3% do salário bruto será de R${:.2f} e o salário líquido será de R${:.2f}".format(desc2,sal_liq2))