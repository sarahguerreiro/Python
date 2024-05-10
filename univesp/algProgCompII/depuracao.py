'''
é o processo de encontrar e reduzir erros em programas.
os erros podem:

- impossibilitar q o prog continue sua exec
- fazer com q o prog gere como saida um resultado incorreto

'''
'''
def h(n):
    print('start h')
    print(1/n)
    print(n)
def g(n):
    print('start g')
    h(n-1)
    print(n)
def f(n):
    print('start f')
    g(n-1)
    print(n)
f(2)
'''
i = [3,4,(2,1)]
i[-1][0] = -1

print(i)