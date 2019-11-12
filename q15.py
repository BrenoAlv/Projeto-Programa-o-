#Jogo de Pedra, papel e tesoura: nesse jogo cada jogador faz sua escolha (1 –Tesoura, 2 – Pedra, 3 – Papel),
# e vence aquele que escolher um objeto que seja capaz de vencer o outro.Faça que leia a opção de objeto do primeiro jogador
# a opção de objeto do segundo jogador e informe qual jogador venceu(ou se houve empate).
print("VAMOS JOGAR PEDRA, PAPEL OU TESOURA!?")
print("\nOpções -->> 1-Tesoura 2-Pedra 3-Papel \nEscolham então!")
escolha1 = int(input("Usuário 1, escolha: "))
escolha2 =int(input("Usuário 2, escolha: "))
# usuário 1
if escolha1 == 1 and escolha2 == 3:
    print("O usuário 1 escolheu Tesoura")
    print("O usuário 2 escolheu Papel")
    print("Tesoura corta papel!")
    print("Usuário 1 ganhou!")
    print("Obrigado por jogarem!")

elif escolha1 == 2 and escolha2 ==1:
    print("O usuário 1 escolheu Pedra ")
    print("O usuário 2 escolheu Tesoura")
    print("Pedra quebra tesoura!")
    print("Usuário 1 ganhou!")
    print("Obrigado por jogarem!")
elif escolha1 == 3 and escolha2 == 2:
    print("O usuário 1 escolheu Papel")
    print("O usuário 2 escolheu Pedra ")
    print("Papel embrulha a pedra!")
    print("Usuário 1 ganhou!")
    print("Obrigado por jogarem!")
# Aqui começa o usuário 2.
elif escolha2 == 1 and escolha1 == 3:
    print("O usuário 1 escolheu Papel ")
    print("O usuário 2 escolheu Tesoura ")
    print("Tesoura corta papel!")
    print("Usuário 2 ganhou!")
    print("Obrigado por jogarem!")
elif escolha2 == 2 and escolha1 ==1:
    print("O usuário 1 escolheu Tesoura")
    print("O usuário 2 escolheu Pedra")
    print("Pedra quebra tesoura!")
    print("Usuário 2 ganhou")
    print("Obrigado por jogarem!")

elif escolha2 == 3 and escolha1 == 2:
    print("O usuário 1 escolheu Pedra")
    print("O usuário 2 escolheu Papel ")
    print("Papel embrulha a pedra!")
    print("Usuário 2 ganhou")
    print("Obrigado por jogarem!")
#Aqui trabalhei a possibilidade de empate
elif escolha1 == 1 and escolha2 == 1:
    print("O usuário 1 escolheu Tesoura")
    print("O usuário 2 escolheu Tesoura ")
    print("EMPATE")
    print("Obrigado por jogarem!")
elif escolha1 == 2 and escolha2 ==2:
    print("O usuário 1 escolheu Pedra ")
    print("O usuário 2 escolheu Pedra")
    print("EMPATE")
    print("Obrigado por jogarem!")
elif escolha1 == 3 and escolha2 == 3:
    print("O usuário 1 escolheu Papel")
    print("O usuário 2 escolheu papel")
    print("EMPATE")
    print("Obrigado por jogarem!")
else:
    print("Por favor, usuários. Digitem somente 1-Tesoura 2-Pedra 3-Papel")
    print("Tente de novo!")