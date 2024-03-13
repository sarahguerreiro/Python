# A soma dos 5 primeiros inteiros positivos.
inteiros_positivos = [1,2, 3, 4, 5, 6, 7, 8, 9,10]
primeiros5 = inteiros_positivos[:5]

print(sum(primeiros5))

# A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
idade_sara = 23
idade_mark = 19
idade_fatima = 31

media_idades = idade_fatima + idade_mark + idade_sara / 3

print(f'a media das idades é {media_idades}')

# O número de vezes que 73 cabe em 403.
valor1 = 73
valor2 = 403
divisao = 403 // 73

print(f'o numero {valor1} cabe {divisao}x em {valor2}')

# O resto de quando 403 é dividido por 73.
resto = valor2 % valor1

print(f'o resto da divisão entre {valor2} e {valor1} é {resto}')

# 2 à 10ª potência.

print(2**10)

# O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
altura_sara = 54
altura_mark = 57

print(abs(altura_mark-altura_sara))

# O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.

valores = [34.99, 29.95, 31.50]

print(min(valores))

s1 = 'ant'
s2 = ' bat'
s3 = ' cod'

#a. 'ant bat cod'
print(f'{s1}{s2}{s3}')

#b. 'ant ant ant ant ant ant ant ant ant ant'
print(f'{s1} '*10)

#c. 'ant bat bat cod cod cod'
print(f'{s1}{2*s2}{3*s3}')

#d. 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
print(f'{s1}{s2} '*7)

#e. 'batbatcod batbatcod batbatcod batbatcod batbatcod'
concat = s2 + s2.strip() + s3.strip()

print(f'{concat}'*5)

# ------------- EXERCICIO 2.2 ---------------

# A soma de 2 e 2 é menor que 4.
print(2+2 < 4)

# O valor de 7 // 3 é igual a 1 + 1.
print(7 // 3 == 1+1) 

# A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
print(3**2 + 4**2 == 25)

# A soma de 2, 4 e 6 é maior que 12.1387 é divisível por 19.
#print(sum(2+4+6) > 121.387 & 121.387 % 19 == 0 )

#31 é par. (Dica: o que o resto lhe diz quando você divide por 2?)
print(31 % 2 == 0)

#O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.*

