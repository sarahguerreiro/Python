""""dia = 20
mes = 'outubro'
ano = 2022

print(dia, mes, ano, sep= ' de ')
"""
"""base = eval(input("Digite a base: ")) 

altura = eval(input("Digite a altura: ")) 

area = (base * altura) / 2 

print("A área é", area)"""

import math 


num = input("Digite um número: ") 

quadrado = math.pow(num, 2) 

cubo = math.pow(num, 3) 

raiz = math.sqrt(num) 

print(f'O numero ao quadrado é {quadrado} e ao cubo é {cubo}') 

print(f'A raiz quadrada é {raiz:.2f}') 

import math

# Recebe o número como uma string e converte para float
num = float(input("Digite um número: "))

# Calcula o quadrado e o cubo diretamente
quadrado = num ** 2
cubo = num ** 3

# Calcula a raiz quadrada
raiz = math.sqrt(num)

# Imprime os resultados
print(f'O número ao quadrado é {quadrado} e ao cubo é {cubo}')
print(f'A raiz quadrada é {raiz:.2f}')