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


