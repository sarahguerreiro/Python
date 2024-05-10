"""def f(v, i): 
    if i == 0: 
        return i 
    else: 
        j = f(v, i - 1) 
        if v[i] > v[j]: 
            return i 
        else: 
            return j 
 
l = [5,4,6,8,1,12] 
print(f(l, len(l) - 1)) 
"""
def binarySearch(array, key):
    comprimento = len(array)
    left = 0
    rigth = -1
    
while (left <= rigth):
    middle = int((left + rigth)/2)
    if array[middle] == key:
        print(meio)
        break
    if key < array[middle]:
        rigth = middle - 1
    if key > array[middle]:
        left = middle + 1
    else:
        print("value not found")