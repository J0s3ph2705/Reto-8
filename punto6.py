#Se toma la base como texto y la potencia como entero
n1=str(input("Base? "))
n2=int(input("Potencia? "))
#Se crea "f", el cual va a multiplicar los dos valores, como uno es texto y el otro es número, escribe el texto tantas veces cómo el número lo indique
f=n1*n2
#Se hace una variable que sirve como base
p=1
#Se determina cuántos elementos terminaron en "f", entonces se multiplica la base por si misma la cantidad de veces que está el número en f (Si hay 3 elementos en f, se multiplica n1 por si mismo 3 veces)
for value in f:
    p=int(n1)*p
#Se imprime el resultado final
print(p)
