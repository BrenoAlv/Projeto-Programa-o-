gratificacao = 0
salario_liquido = float(input('Digite o salario: '))

if salario_liquido < 2000:
    gratificacao = '5%'
    salario_liquido2 = salario_liquido+(salario_liquido * 5)/100
elif salario_liquido >= 2000 and salario_liquido <= 2500:
    gratificacao = '10%'
    salario_liquido2 = salario_liquido+(salario_liquido * 10)/100
elif salario_liquido > 2500 and salario_liquido <= 3000:
    gratificacao = '15%'
    salario_liquido2 = salario_liquido+(salario_liquido * 15) / 100
elif salario_liquido > 3000:
    gratificacao = '20%'
    salario_liquido2 = salario_liquido+(salario_liquido * 20) / 100

print('Gratificacao:', gratificacao)
print('Salario Liquido:', salario_liquido2)