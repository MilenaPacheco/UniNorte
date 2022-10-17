def mayusculas(texto):
    separo=texto.split()
    devolucion=f"{separo[0].capitalize()} {separo[1].capitalize()}"
    return devolucion

def aplicar(funcion,lista):
    nueva = [] 
    for n in lista: #lista es personas
        nueva.append(funcion(n))
    return nueva

personas = ["juan salvo", "henry courtney", "elizabeth bennet", "marge simpson"]
print(aplicar(mayusculas,personas))