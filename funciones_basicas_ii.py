# 1-cuenta regresiva
print("//cuenta regresiva//")
def countdown(numero):
    arrays = []
    for i in range(numero,-1,-1):
        arrays.append(i)    
    return arrays
result = countdown(5) 
print(result)

# 2-Imprimir y Devolver
print("///// 2-Imprimir y Devolver/////")
def print_y_return(arr):
    print(arr[0])
    return arr[1]

resultado = print_y_return([1,2]) 
print(resultado)

print("/////// 3-Primero más longitud//////////")
# 3-Primero más longitud
def primero_mas_largo(arr):
    return arr[0]+len(arr)
resultado = primero_mas_largo([1,2,3,4,5]) 
print(resultado)

print("/// 4-valores ​​mayores que el segundo///")
# 4-valores ​​mayores que el segundo
def valores_mayores_que_el_segundo(arr):
    newlist=[]
    if len(arr)<2:
        return False
    else:
        for i in arr:
            if i>arr[1]:
                newlist.append(i)
    print(len(newlist))
    return newlist
resultado=valores_greater_than_second([5,2,3,2,1,4])
print(resultado)

print("//// 5-Esta longitud Ese Valor/////")
# 5-Esta longitud Ese Valor
def longitud_y_valor(a,b):
    newArray = []
    for i in range(0,a):
        newArray.append(b)
    return newArray
resultado1=longitud_y_valor(4,7)
print(resultado1)
resultado2=longitud_y_valor(6,2)
print(resultado2)