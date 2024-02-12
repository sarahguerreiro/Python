"""Primeiro, execute a atribuição palavras =
['taco', 'bola', 'celeiro', 'cesta', 'peteca']
Agora, escreva duas expressões Python que são avaliadas, respectivamente, como a
primeira e a última palavras em palavras, na ordem do dicionário.
"""

palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']

primeira_palavra = sorted(palavras)[0]
ultima_palavra = sorted(palavras)[-1]

print('Primeira palavra: ', primeira_palavra)
print('Última palavra: ', ultima_palavra)
