numero1 = int(input('Digite o numero 1: '))
numero2 = int(input('Digite o numero 2: '))
numero3 = int(input('Digite o numero 3: '))

maior = 0


if numero2 < numero1 and numero1 > numero3:
    maior = numero1
    print('Maior numero:', maior)
elif numero1 < numero2 > numero3:
    maior = numero2
    print('Maior numero:', maior)
elif numero1 < numero3 > numero2:
    maior = numero3
    print('Maior numero:', maior)
else:
    print('Os valores digitados não são diferentes')