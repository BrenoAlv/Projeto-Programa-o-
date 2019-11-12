peso = float(input('Olá vamos calcular o seu IMC, Por favor, me informe o seu peso atual: '))
alt = float(input('Agora me informe sua altura atual: '))
calc_imc = peso / (alt**2)
if calc_imc <= 18.5:
    print('Seu peso atual é de {}Kg, Sua altura atual é de {}m, Seu IMC é de {:.2f}, Você está bem abaixo do peso ideal, procure ajuda profissional!'.format(peso, alt, calc_imc))
elif calc_imc > 18.5 and calc_imc <= 24.9:
    print('Seu peso atual é de {}Kg, Sua altura atual é de {}m, Seu IMC é de {:.2f}, Você está no peso ideal!'.format(peso, alt, calc_imc))
elif calc_imc >= 25.0 and calc_imc <= 29.9:
    print('Seu peso atual é de {}Kg, Sua altura atual é de {}m, Seu IMC é de {:.2f}, Você está com sobrepeso!'.format(peso, alt, calc_imc))
elif calc_imc >= 30.0 and calc_imc <= 39.9:
    print('Seu peso atual é de {}Kg, Sua altura atual é de {}m, Seu IMC é de {:.2f}, Você está bem acima do peso ideal, procure ajuda profissional!'.format(peso, alt, calc_imc))
else:
    print('Seu peso atual é de {}Kg, Sua altura atual é de {}m, Seu IMC é de {:.2f}, Você está muito acima do peso ideal, procure ajuda profissional!'.format(peso, alt, calc_imc))