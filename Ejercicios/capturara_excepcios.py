def solicitar_num(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Hay un error")

a=solicitar_num("Ingrese un número")
b=solicitar_num("Ingrese otro número")

print(a+b)
print(a-b)
print(a*b)
try:
    print(a/b)
except ZeroDivisionError:
    print("No se puede dividir por cero")

