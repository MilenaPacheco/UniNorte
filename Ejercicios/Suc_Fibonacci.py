#num=int(input("Ingrese la cantidad de números de la serie a mostrar: "))

def fibo(num):
    if num <= 2:
        print("Ingrese un valor mayor a 2")
    lista=[0,1]
    while len(lista)<num:
        suma=lista[-1]+lista[-2]
        lista.append(suma)
    return lista

print (fibo(1))
print (fibo(10))
