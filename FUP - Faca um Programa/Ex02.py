print("Fórmula para conversão da temperatura de graus Celsius para Fahrenheit: F = C × 9 / 5 + 32.")

temperatura = float(input("Escreva sua temperatura em Celsius para converter para Fahrenheit: "))
temperatura_convertida = temperatura * 9 / 5 + 32

print(f"Sua temperatura convertida para Fahrenheit ficou: {temperatura_convertida:.1f} °F")