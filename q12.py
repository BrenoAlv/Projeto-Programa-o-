salbrt = float(input('Olá, Por favor me informe seu salário: '))
inss = salbrt*0.10
ir = salbrt*0.25
sindicato = salbrt*0.005
contribuição = abs(inss+ir+sindicato)
salliq = salbrt-contribuição
print('O valor das contribuições foram:\nINSS: R${:.2f}\nIR: R${:.2f}\nSindicato: R${:.2f}\n\nTotal: R${:.2f}'.format(inss, ir, sindicato, contribuição))
print('\nSeu Salário Liquído é de R${:.2f}'.format(salliq))