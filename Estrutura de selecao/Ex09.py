valor = float(input("Digite o valor da sua compra: "))

if valor < 100:
    print(f"O valor da compra é de: R$ {valor}. ")
else:
    desconto = valor * 0.1
    valor_descontado = valor - desconto
    print(f"O valor ganhou desconto de 10%, o valor descontado ficou: R$ {valor_descontado}")
