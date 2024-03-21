#Se toma como base el 1 porque es la primera tabla, p que va a ser el valor que multiplica a la base y c que va a ser el resultado de las multiplicaciones
n=1
p=1
c=1
#Se imprime el títlo de la primera tabla
print("Tabla del "+str(n))
for p in range(0,11):
#Se hace la multiplicación entre la base (n) y el multiplicador (p) que da un resultado (c), se imprimen los 3 y se añade uno al multiplicador, esto se repite hasta que el multiplicador llegue a 10
    while n<=10:
        c=n*p
        print(str(n)+" por "+str(p)+" es igual a "+str(c))
        p+=1
#Cuando el multiplicador llegue a 10, se añade uno a la base y se restituyen los otros valores a 1, luego se uimprime el título del número que sigue, hasta llegar a la tabla del 10.
        if 10*n==c and n<=10:
            n=n+1
            p=1
            c=1
            if n<=10:
                print("Tabla del "+str(n))
