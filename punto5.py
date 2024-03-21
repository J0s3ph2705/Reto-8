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
