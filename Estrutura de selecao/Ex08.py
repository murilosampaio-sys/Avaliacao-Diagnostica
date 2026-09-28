idade = int(input("Digite sua idade em anos de vida: "))

if idade < 0:
    print("Digite um número válido (idade não pode ser negativa).")

elif idade < 12:
    texto_ano = "ano" if idade == 1 else "anos"
    print(f"Sua idade de {idade} {texto_ano} é de criança.")

elif idade < 18:
    print(f"Sua idade de {idade} anos é de adolescente.")

else:
    print(f"Sua idade de {idade} anos é de maior.")