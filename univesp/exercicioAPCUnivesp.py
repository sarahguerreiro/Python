"""Ler uma temperatura em graus Celsius e apresentá-la convertida
em graus Fahrenheit. A fórmula de conversão é F ← C * 9 / 5 + 32,
sendo F a temperatura em Fahrenheit e C a temperatura em Celsius:

começo iniciando uma função que recebe o valor em celsius e retorna o valor convertido pra fahrenheit:
"""

def converte_celsius_fahrenheit(celsius):

    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

# Recebe do user a temp em celsius:

celsius = float(input("Digite a temperatura em graus Celsius: "))

# converte pra Fahrenheit:

fahrenheit = converte_celsius_fahrenheit(celsius);

# Apresenta o resultado:

print(f"Sua temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
