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
