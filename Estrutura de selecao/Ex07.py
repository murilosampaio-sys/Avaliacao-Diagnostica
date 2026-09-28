numero1 = int(input("Digite um número para ver se ele é maior ou menor: "))
numero2 = int(input("Digite outro para ver se ele é maior ou menor: "))
numero3 = int(input("Digite outro para ver se ele é maior ou menor: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"O {numero1} é o maior número.")

elif numero2 > numero1 and numero2 > numero3:
    print(f"O {numero2} é o maior número.")

elif numero3 > numero1 and numero3 > numero2:
    print(f"O {numero3} é o maior número.")

else:
    print("Dois ou mais números são iguais e empataram no maior valor.")