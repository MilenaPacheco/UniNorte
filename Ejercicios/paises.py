paises= {"ar": "Argentina", "es": "España", "us": "Estados Unidos", "fr": "Francia"}

while True:
    codigo=input("Ingrese el código del país: ")
    if codigo == "Salir":
        break
    try:
        print(paises(codigo))
    except KeyError:
        print("El código es ínvalido")


