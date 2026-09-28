import random

numero_certo = random.randint(1, 100)

chute = int(input("Digite um número de 1 a 100 para adivinhar: "))

while chute != numero_certo:
    if chute > numero_certo:
        print("Seu chute é MAIOR que o número certo!")
    else:
        print("Seu chute é MENOR que o número certo!")
    
    chute = int(input("Tente outro número: "))

print(f"Parabéns! Você acertou o número {numero_certo}!")