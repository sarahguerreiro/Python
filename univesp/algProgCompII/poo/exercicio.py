def imc(peso, altura_cm):
    altura_m = altura_cm / 100
    calc = peso / (altura_m ** 2)
    
    if calc < 18.5:
        return "abaixo do pesoo"
    elif 18.5 <= calc < 24.9:
        return "normal"
    elif 25 <= calc < 29.9:
        return "sobrepeso"
    else:
        return "obesidade"
          
print(imc(70, 168))


s = 'monteiro-lopes'
#laço de iteraçao: usado para percorrer os caracteres de uma string
for c in s:
 if c in 'aeiou':
        print(c) 
        
        
        
n = 10
#laço contador: quando precisar executar um bloco de código p cada inteiro em algum itervalo(range)
for i in range(n):
  if i % 2 == 0:
     print(i, end = ' ')

     
     
def potencias(n):
    for i in range(1, n +1):
        print(2 ** i, end=' ')
potencias(6)

#Laço acumulador: O laço for percorre os números na listaNum. A cada iteração, o número atual é somado ao acumulador minhaSoma usando a atribuição minhaSoma = minhaSoma + num:

listaMun = [3, 2, 7, -1, 9]
minhaSoma = 0
for num in listaMun:
  minhaSoma+=num
print(minhaSoma)
      