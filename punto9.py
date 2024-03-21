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
