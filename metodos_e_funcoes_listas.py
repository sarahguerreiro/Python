# METODOS DE LISTAS: É como se fosse uma função atrelada a uma var

lista = [1, 3, 12, 8, 2]

# APPEND - Metodo usado quando vc precisa adcionar um elemento ao final de uma lista

print('antes do append', lista)
lista.append(3)
print('depois do append', lista)

# INSERT - Adc um elemento a um local especifico da lista, em que vc escolhe/seta

lista.insert(2, 10)

print('Depois do insert: ', lista)



# EXTEND - Unindo duas listas/array

lista2 = [1, 2, 3]

lista.extend(lista2)

print('depois do extend: ', lista)


# POP - Metodo de remoçao de elementos de uma lista. Se vc nao passar nenhum valor como paramentro, ele vai tirar o ultimo elemento da lista; mas vc pode especificar qual elemento em especifico vc quer tirar passando o valor de seu indice entre parentese:

lista.pop(1)

print('lista apos o pop: ', lista)


# REMOVE - Aqui o q vc passa ao paramentro é o elemento em si a ser removido. Detalhe, ele só remove o primeiro elemento q ele encontrar, e nao todos os q forem == ao valor setado entre parentese: 


lista.remove(3)

print('depois do remove: ', lista)


# COUNT - Com esse metodo vc consegue contar quantas x um elemento, setado entre parenteses, aparece na lista:  

print('Quantidade de 2 na lista: ', lista.count(2))


# INDEX - Te diz o índice de determinado elemento num array:  

print('indice do elemento 12: ', lista.index(8))

# SORT - Método que serve pra ordenar sua lista:

lista.sort()
lista.sort(reverse=True)
print(lista)





