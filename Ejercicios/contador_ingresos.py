personas=["Susana","Tamara","Ana","Susana","Susana","Tomas","Ana"]
ingresos={}
for i in personas:
    if i not in ingresos:
        ingresos[i] = 1
    else:
        ingresos[i]+=1
print(ingresos)