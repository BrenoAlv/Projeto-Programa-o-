credito = 0
saldo_medio = int(input('Digite o saldo medio: '))

print(' O saldo medio é :', saldo_medio)

if saldo_medio >= 0 and saldo_medio < 200:
    print('Nenhum crédito')

elif saldo_medio >= 201 and saldo_medio <= 400:
    print('O valor do crédito: ', int(saldo_medio*0.2))
elif saldo_medio >= 401 and saldo_medio <= 600:
    print('O valor do crédito: ', int(saldo_medio*0.3))
elif saldo_medio > 601:
    print('O valor do crédito: ', int(saldo_medio*0.4))