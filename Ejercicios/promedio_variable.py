def promedio_variable(*args):
    suma = 0
    for i in args:
        suma+=i
    promedio = suma/len(args)
    return promedio
print(promedio_variable(10,8,9))