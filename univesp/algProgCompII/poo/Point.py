class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
# o metodo __init__ é chamado automaticamente ao se instanciar um objeto desta classe
    def setx(self, x):
        self.x = x
        
    def sety(self, y):
        self.y = y
        
    def get(self):
        return self.x, self.y
    
    def move(self, offsetx, offsety):
        self.x +=  offsetx
        self.y +=  offsety
        
    def __add__(self, other):
       if type(other) == Point:
           return Point(self.x + other.x, self.y + other.y)
       else:
           return Point(self.x + other, self.y + other)
# a depender do operando(other), a operação será feita entre x e x ou x e y. por ex:
# x + y ==> (2,3) + (2,2) ==> (4,5)
# x + 8 ==> (2,3) + 8 ==> (10, 11)
        
    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
#sem o uso desse metodo, seu output no terminal sera a reperesentação padrão <__main__.Point object at 0x1048b8400> e nao o output esperado
        
        
objeto1 = Point()
objeto1.setx(5)
#objeto1.move(3, -5)
print(objeto1)

obj2 = Point(3,4)
print(obj2)

print(objeto1 + obj2)