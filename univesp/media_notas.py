"""
Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno
representadas pelas variáveis N1, N2, N3 e N4. Calcular a média aritmética
(variável MD) desse aluno e apresentar a mensagem “Aluno Aprovado com média” se a
média obtida for maior ou igual a 5; caso contrário, apresentar a mensagem “Aluno
Reprovado com média”. Informar também, após a apresentação das mensagens, o valor
da média obtida pelo aluno.

"""

# inicio as variaveis dadas no problema com o input para que o user possa passar dinamicamente e adiciono um float na frente pra transformar a entrada do user em um numero:

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

# agora, tiro a mmedia aritmetica das notas:

md = (n1+n2+n3+n4) / 4

# teste seletivo que verifica se o aluno foi o não aprovado:

if md >= 5:
    print("Aluno aprovado com a média de: ", md)
else:
    print("Aluno reprovado com média de: ", md)