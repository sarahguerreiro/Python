'''
Observe q no codigo abaixo seria possivel usar um if/else mas vc nao teria a possibilidade de retornar para o user a possibilidade de outra tentativa, ja com o while, enqanto sua afirmacao nao for satisfeita,o pc vai dar como output  sua msg de print. ATENÇÃO: Note tbm q se vc deixa de repetir a var q carrega a resposta do user abaixo do print de resposta dentro do while, vc vai criar um loop infinito com o output desse print simplesmente pq esse print está apenas carregando uma msg q deve ser repetida infinitamente enquanto sua afirmação nao estiver sendo satisfeita. Ou seja, adc mais 1x a var em questao dentro do bloco de codigo do while apos sua msg de erro, vc força o pc a ler mais uma linha de codigo qe cessa o loop de printar uma msg, pois em mais essa linha ha uma interação com o user q interrompe o loop, reiniciando o processo.
'''

numero_sorteado = 15

numero_escolhido = int(input('Informe um número entre 1 e 20:'))

while numero_escolhido != numero_sorteado:
    print('Voce errou o número. Tente novamente!')
    numero_escolhido = int(input('Informe um número entre 1 e 20:'))
