
'''
o for é uma estrutura de repetição feita praser usada quando vc tem um numero total de vezes em que vc quer q aconteç essa repetição
o range é usado quando vc quer contar uma faixa especifica de numeros q vc coloca entrw aspas depois da palara reservada range 

range vai de 0 ate o numero setado -1:

for i in range(6):
    print(i)
    
'''


'''
range com valor de inicio e valor de parada:

for i in range(1, 11 ):
    print(i)
'''

'''
range com 3 paramentros: valor de inicio, valor de parada e passo (step) q indica de quanto em quanto vc quer pular o valor:

for i in range(1, 122, 4):
    print(i)
'''

soma = 0

for i in range(1,4):
    nota = float(input(f'informe a sua nota: {i}: '))

    soma = soma + nota
print(soma/3)

'''
INJETANDO UMA VAR DENTRO DE UMA STRING: 
 Como a var i é o q vai mudar a cada iteração, 
 é ela q vc vai injetar na string do input, 
 adc um f na frente da string em questão,logo antes d as aspas, o q vai indicar q será feita uma injeção naquela string, depois vc so precisa abrir chaves na posição q vc quer q a var esteja na string e coloca a var dentro
'''
#VARIÁVEL ACUMULADORA: é quando vc cria uma var com o 0 por ser um numero neutro e adc essa var no bloco de codico reatribuindo o valor dela a soma dela mesma + valor recebido do user 


