#Nuevamente, este funciona con el número que se pida, entonces se pide el número
p=int(input("Número? "))
#Se determiina una variable para los números pares y otra para los impares
n=1
t=2
#Se señala cuáles van a ser los números impares
print("Números impares: ")
#Se van imprimiendo los números de 1 hasta el número, de dos en dos
for n in range(1,p+1,2):
    print(str(n))
    n+=2
#Se señala cuáles van a ser los números pares
print("Números pares: ")
#Se van imprimiendo los números de 2 hasta el número, de dos en dos
for t in range(2,p+1,2):
    print(str(t))
    t+=2
