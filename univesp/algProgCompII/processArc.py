'''
crio uma variavel q vai carregar o arquivo passado como parametro:

arquivo = open('../semana2/exercicioString.py', 'r')

entao crio uma var que vai carregar a leitura desse arquivo:

conteudo = arquivo.read()

printo conteudo na tela:

print(conteudo)

sempre depois de consultar um arquivo, utiliza-se o metodo close para avisar o sistema que libere os recursos/infos sobre o arquivo aberto: 

close()
'''
def readFile(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordList = content.split()
    print(wordList)
    return len(wordList), len(content)
n_words, n_chars = readFile('test.txt')


''''
--------------- EXERCICIO ------------------

infile.read(n)

infile.read()

infile.readlines()

outfile.write(s)

outfile = open('test.txt', 'w')

file.close()

'''

# Para escrever outros tipos de dados, alem d e string, devemos converte-los ou usar o metodo format():

# >>> idade = 30
# >>> outfile.write('sua idade é {} anos.\n')
# >>> outfile.write('sua idade é {} anos.\n'.format(idade))