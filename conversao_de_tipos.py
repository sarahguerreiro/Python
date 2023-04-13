'''
comandos pra conversao: 

int()
str()
float()
bool()

'''
idade = '20'
numero1 = 20
numero2 = 'vinte'

print(idade, type(idade))

idade_inteira = int(idade)

print(idade_inteira, type(idade_inteira))
# os valores recebidos pelo input são sempre entendidos pelo py como str, caso vc saiba com ctz q os valores q o user fornecerá é em número, envolva o input com o comando referente a conversão q vc quer fazer, nesse caso podendo ser float [para numeros quebrados] ou int [para numeros inteiros]
altura = float(input('informe sua altura: '))
print(altura, type(altura))