def comparar_listas(primera, segunda):
    num_rep = []
    for i in primera:
        for n in segunda:
            if n == i and n not in num_rep:
                num_rep.append(i)
            else:
                continue

    return num_rep
primera=[7,5,10,9,8,1,3,5,6,3,8,0,10,9,2]
segunda=[6,9,3,7,9,10,5,10,7,4,5,3,2,10,2]
print(comparar_listas(primera,segunda))

#Otra manera más resumida de hacerlo
tercera=[]
for n in primera:
    if n in segunda and n not in tercera:
        tercera.append(n)
print(tercera)