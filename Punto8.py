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
