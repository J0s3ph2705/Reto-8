# Reto-8
1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
 ```python
#Se toma el número límite (En este caso puede ser 100, sino que quise acerlo para que funcionara con cualquier número)
p=int(input("Número? "))
#Se hace una variable que va a aumentar hasta el número que se pidió
n=1
#Se hace el loop que saca el cuadrado del número, imprime el número con su cuadrado y aumenta el valor de ´n´ hasta que llegue al número pedido.
for n in range(1,p+1):
    f=n**2
    print(str(n)+" al cuadrado es "+str(f))
    n+=1
``` 
2.  Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
  ```python
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
```  
3.  Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
  ```python
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
```  
4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
  ```python
# Se toma el número
n=int(input("Número? "))
#Se determinan la variable f para llevar la cuenta y el i como la base del factorial
f=1
i=1
#Se determina el rango entre 1 y el número
for i in range(1, n+1):
#Se multiplica el número de cuenta con la base, se le adiciona 1 a la base y se imprime la cuenta
    f=f*i
    i+=1
    print(f)
```
5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.
   ```python
#Se toma la potencia
n=int(input("Potencia? "))
#Se potencia 2 al número y se imprime
for n in range(n, n+1):
    p=2**n
    print(p)
```
6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. **Disclaimer:** Trate de no utilizar el operador de potencia (**).
   ```python
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
```
7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
   ```python
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
```
8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
 ```python
#Se determina varias variables base, primero el número que la persona ponga, un número inicial que va a servir como factorial y guía de todo el código, el exponente que potencia a x, el exponente de las derivadas
numero=float(input("Número? "))
inicial=float(1)
expo=float(0)
expo_derivada=float(2)
#Se determinan otras variables, "d" que va a llevar la cuanta factorial, e que es el número euler exacto pero sin decimales (no sé por qué no me funcionaba si ponía decimales, igual multipliqué al número por un decimal para que no se alterara el resultado) y una lista para llevar los valores que nos da cada ciclo
d=float(1)
e=float(271828)
lista=[]
#Se determina que el ciclo dure hasta que el número guía alcance al número indicado 
while inicial<=numero:
#Se desarrolla la función o la derivada
    f=(e*10**-7)**expo
#Se desarrolla la potencia
    p=numero**expo
#Se desarrolla el factorial
    d=inicial*inicial
#Se unen los resultados para sacar un ciclo
    maclaurin=f/d*p
#Se saca la base de la derivada de la función o derivada anterior
    e=e*expo_derivada
#Se añade 1 al número inicial, al exponente del número y se resta 1 al exponente de la derivada
    inicial +=1
    expo +=1
    expo_derivada=-1
#Se pone el resultado en la lista
    lista.append(maclaurin)
#Se suman los elementos y se imprime
total=sum(lista)
print(total)

```
9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
 ```python
#Todo es casi igual, excepto la función, se reemplaza por la función de seno
import math
numero=float(input("Número de ciclos? "))
inicial=float(1)
expo=float(0)
expo_derivada=float(2)
d=float(1)
e=float(271828)
lista=[]
while inicial<=numero:
    f=math.sin(0)**inicial
    p=numero**expo
    d=inicial*inicial
    e=e*expo_derivada
    maclaurin=f/d*p
    inicial +=1
    expo +=1
    expo_derivada=-1
    lista.append(maclaurin)
total=sum(lista)
print(total)
```
10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
 ```python
#Todo es casi igual, excepto la función, se reemplaza por la función de arcotangente
import math
numero=float(input("Número de ciclos? "))
inicial=float(1)
expo=float(0)
expo_derivada=float(2)
d=float(1)
e=float(271828)
lista=[]
while inicial<=numero:
    f=math.atan(0)**inicial
    p=numero**expo
    d=inicial*inicial
    e=e*expo_derivada
    maclaurin=f/d*p
    inicial +=1
    expo +=1
    expo_derivada=-1
    lista.append(maclaurin)
total=sum(lista)
print(total)
```
