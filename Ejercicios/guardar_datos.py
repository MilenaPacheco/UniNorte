personas = {"juan":20, "Romina":32, "Tamara":42}
try:    
    with open ("personas.txt", "w") as f:
        for i in personas:
            texto=f.write(f"{i.lower()}-{personas[i]}"+"\n")
        print("Salvado")
except FileNotFoundError:
    print("No se puede grabar")    


 