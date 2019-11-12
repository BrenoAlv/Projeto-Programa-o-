#8.Sejam P(x1,y1) e Q(x2,y2) dois pontos quaisquer do plano. A sua distância é dada por:
#D = (Raiz) (x2 – x1)2 + (y2 – y1)2
#Elabore um programa que leia as coordenadas dos pontos “P” e “Q”, calcule e escreva sua distância.

print("Digite as coordernadas do PONTO P ")
x1 = int(input("Digite o valor de x1: "))
y1 = int(input("Digite o valor de y1: "))

print("Digite as coordernadas do PONTO Q")
x2 = int(input("Digite o valor de x2: "))
y2 = int(input("Digite o valor de y2: "))

D=(x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)
import math
a = math.sqrt(D)

print("A distância entre eles é {:.2f}".format(a))