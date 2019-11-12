tempo=float(input('Qual o tempo de viagem? '))
velocidade=int(input('Qual foi a velocidade Km/h média ? '))
distancia=tempo*velocidade
consumo=distancia/12
print('Velocidade: {}Km/h'.format(velocidade))
print('Tempo de viagem:{:.2f} min.'.format(tempo*60))
print('Distância percorrida: {:.2f}Km'.format(distancia))
print('Consumo de combustível: {:.2f}L'.format(consumo))