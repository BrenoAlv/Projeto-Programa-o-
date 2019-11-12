total = 0
while (True):
    print('------------LANCHONETE------------')
    print('Olá, confira nosso cardápio, fique à vontade!\n\nCachorro Quente| cód. 100| preço R$5,20\nHambúrguer| cód. 101| preço ''R$5,20\nCheeseburguer| cód 102| preço R$7,30\nRefrigerante| cód 103| preço R$5,00')
    codigo=int(input("Digite o código do lanche: "))
    qtd = int(input("Digite a quantidade: "))
    if codigo == 100:
        total = total + 5.20*qtd
    elif codigo == 101:
        total = total + 5.20*qtd
    elif codigo == 102:
        total = total + 7.30*qtd
    elif codigo == 103:
        total = total + 5.00*qtd
    elif codigo < 100 or codigo > 103:
        print("Código inválido!")
        continue
    fim = input("Deseja continuar a compra? ")
    if fim == "s" or fim == "S":
        continue
    elif fim == "n" or fim == "N":
        break
print("O total a pagar será R$ {:.2f}, Obrigado Volte Sempre!".format(total))

