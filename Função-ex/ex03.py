<<<<<<< HEAD
#Gerador de numeros aleatorios
import random

def gerar_numero_aleatorio(n, m):
    if n > m:
        aleatorio = random.randint(m, n)
    else: 
        aleatorio = random.randint(n, m)
    return aleatorio

n = int(input("Digite um numero: "))
m = int(input("Digite outro numero: "))

numero_aleatorio = gerar_numero_aleatorio(n, m)
print(numero_aleatorio)
=======
for i in range(0, 52, 2):
    print(i)
>>>>>>> 356f9c7db0d01f814c9ef6c49e9c330222580ab6
