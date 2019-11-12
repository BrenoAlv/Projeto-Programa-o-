masc=0
femi=0
user=0
apro=0
print('E para finalizar')
while user !='E'or user != 'e' or apro!='E'or apro!='e':
    user=input('Digite [M] Masculino [F] Feminino Ou Aprovado [A]: ')
    if user=='M'or user =='m':
        masc=masc+1
    elif user=='F'or user=='f':
        femi=femi+1
    elif user=='A'or user=='a':
        apro=apro+1
    elif user== 'E' or user =='e':
        break
pessoas=masc+femi
h=masc*100/pessoas
m=femi*100/pessoas
aprov=apro*100/pessoas
print('Pessoas:',pessoas,'= 100%')
print('Masculino: {:.2f}%'.format(h))
print('Feminino: {:.2f}%'.format(m))
print('Aprovados: {:.2f}%'.format(aprov))