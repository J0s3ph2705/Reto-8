1.
#Se toma el número límite (En este caso puede ser 100, sino que quise acerlo para que funcionara con cualquier número)
p=int(input("Número? "))
#Se hace una variable que va a aumentar hasta el número que se pidió
n=1
#Se hace el loop que saca el cuadrado del número, imprime el número con su cuadrado y aumenta el valor de ´n´ hasta que llegue al número pedido.
for n in range(1,p+1):
    f=n**2
    print(str(n)+" al cuadrado es "+str(f))
    n+=1
