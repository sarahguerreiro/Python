"""
------------- STRINGS EM PYTHON ---------------
 ALEM DE VARIAVEIS DO TIPO NUMERICO (int, float), 
 E DO TIPO LOGICO (bool),
 PYTHON TBM PERMITE DEFINIR VARIAVEIS DE TIPOS MAIS COMPLEXOS, COMO O str.
 O TIPO str É USADO P REPRESENTAR E MANIPULAR TEXTO OU UMA SEQUENCIA DE CARACTERES, INCLUINDO ESPAÇO EM BRANCO, PONTUAÇÃO E SIMBOLOS DIFERENTES
"""

#----- OPERADORES Q FUNCIONAM COM STRINGS -----

s = 'abcd'
# atribuição

print(s == 'abc')
# comparação

t = 'defg'
# atribuição

print(s < t)
# comparação menor que

print(s + t)
# soma: ele vai concatenar as strings

print(s * 2)
# multiplicação: ele vai pegar o valor da string e vai fazer um clone dele
# print(s * t)
# ERR: entretando a multiplicação so vai funcionar se for entre uma string e um numero inteiro

ch = 'b'
print(ch in s)
# comparação: ele compara o valor de ch com o valor de s e se algum valor de ch estiver contido em s ele retorna true

print(ch is str('b'))
# verifica se o valor de ch é = ao que esta sendo passado entre aspas simples 

"""
--- OPERADORES Q NÃO FUNCIONAM COM STRINGS ---
- SUBTRAÇÃO
/ DIVISÃO
// QUOCIENTE
% RESTO
** POTENCIA

"""

#------- OPERADORES/FUNÇÕES IMPORTANTES-------

print(len(ch))
# len() retorna o tamanho da string, mas lembre-se que  pra sair no console é preciso usar dentro de print()

print(len(s))
print(s[0])
print(s[2])
print(s[len(ch)])
# os [] são os OPERADORES DE INDEXAÇÃO. É com eles que  vc pode acessar cada item de um array , da esquerda pra direita, a partir da sua posiçao, que é passada entre colchetes, começando a contar do 0. 
# Tbm é possivel acessar os indices dessa string da direita pra esquerda, com indices negativos, mas ATENÇÃO: 
# para acessar a posição usando indices negativos conte a posição partindo de -1:
#      a  b  c
#      0  1  2
#     -3 -2 -1

print(s[-1])
print(s[-2])
print(s[-3])

# tbm é possivel capturar elementos de um determinado range, que vc estabelece indicando o valor da posição inicial seguido por : seguido pelo valor da  posição final (este valor não sairá no output do console, ele apenas marca o final do range) tudo isso entre colchetes, acessando o que é chamado de substring, assim:

print(s[0:2])
# a substring acima tras o valor ab, referentes a posição 0 e 1.

print(s[-3:-1])

print(s[:3])
# quando vc quiser tudo de uma string ate uma determinada posiçao final, vc usa os colchetes , indicando q o q quer pegar é a posição, usa os dois pontos e coloca o valor da sua posição final, como feito acima. 

print(s[-1:])
# vc tbm pode precisar pegar tudo a partir de uma determinada posição, entao, é so fazer o inverso: o 1o valor entre colchetes é o ponto de partida e depois dos pontos não se coloca valor nenhum, e assim vc consegue pegar tudo



# MAIS MÉTODOS UTEIS

print(s.find('a'))
# o .find retorna o indice(posição) em que o valor passado entre aspas simples está na string

print(s.count('d'))
# o metodo .count retorna a frequencia em q o valor passado entre aspas, ou seja, a substring d, aparece na string s

print(s.replace('d','a'))
# substitui a substring d pela substring a

print(s.capitalize())
# deixa o primeiro caractere de s em maiuscula

print(s.upper())
# transforma todos os caracteres de s em maiuscula

print(s.lower())
# transforma todos os caracteres de s em minuscula

print(s.strip())
# quando vc quiser remover espaços emm branco em excesso, esse metodo faz isiso por vc


