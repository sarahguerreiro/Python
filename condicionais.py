'''
idade = 8 
if idade >= 18:
    print('vc é maior de idade.')
else:
    print('vc é menor de idade.')


********imagine q vc queira imprimir 'aprovado(a)', caso o estudante tenha uma média superior ou igual a 7, e 'reprovado', caso a media seja inferior a 7: ************

nota = float(input('informe sua nota: '))
if nota >= 7:
    print('Aprovado') 

elif nota >= 5:
    print('Recuperação')

else: 
    print('Reprovado')

'''

#operações conjuntas

media = 8 
presenca = 71
if media >=7 and presenca >=70:
    print('Aprovado!')
else:
    print('Reprovado.')
