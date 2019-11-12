nota1=float(input('Digite 1º nota: '))
nota2=float(input('Digite 2º nota: '))
media=(nota1+nota2)/2
if media >=7:
    print('Você está aprovado!')

elif media <7:
    print("Você não está aprovado ainda, digite o valor da 3ª nota abaixo!")
    nota3 = float(input('Digite a 3º nota: '))
    media2 = (nota1+nota2+nota3)/3
    if media2 >=6:
        print('Aprovado! Sua média é : {:.2f}'.format(media2))
    elif media2 <=6:
        print('Reprovado! Sua média é : {:.2f}'.format(media2))
