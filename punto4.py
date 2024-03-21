#Se toma el número
p=int(input("Número? "))
#Se crea una lista para tener los datos de los números pares
l=[]
#Se hace el loop para el rango entre 2 y el número
for p in range(2,p+1):
#Se determina si el número es par o impar, si es impar se le resta uno y se continúa, si es par se añade el número a la lista y se restan 2
    if p%2==0:
        l.append(p)
        p=p-1
    else:
        p-=1
#Se organiza la lista descendentemente y se imprime.
l.sort(reverse=True)
print(l)
