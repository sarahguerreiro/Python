# LISTAS: a lista é uma estrutura de dados. Uma var que armazena varios tipos de var dentro dela, ou melhor, uma coleção de var's

# Sem listas:
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista

notas = [7.9, 9.7, 8.2]

# Criando Listas

Listas = [] #listas vazias podem ser usadas junto a um metodo pra adc itens aos poucos nela

lista = list() # converte uma estrutura em lista

lista = [28,'Guerreiro', 3.856, False]

lista_de_listas = [10, [20, 3, 4], [2, 50, 9]]


'''
INDEXAÇÃO: uma forma de acessar um elemento da lista por meio de um índice 
vc tbm pode acessar itens da lista usando de numeros negativos, seu output será o ultimo valor da lista, ou seja, o 1 valor da direita pra esquerda

'''
lista = [28,'Guerreiro', 3.856, False]
print(lista[1])

'''

SLICE: Ou Fatiamento, é uma forma de vc capturar pedaços de uma lista, fatiando-a de fato:

'''

listado = [10, 50,'listado', 30, 40, 25, 60, 5]
print(listado[2:5])
print(listado[0:3])
print(listado[3:5])
print(listado[4])
print(listado[2:6:2])

# Iteracões com FOR



# 1. Utilizando os proprios elementos da lista

'''for elemento in listado:
    print(elemento)
'''

# 2. Utilizando os índices

print('comprimento de Listado: ', len(listado))

for i in range(len(listado)):
    print(listado[4])
 


