<<<<<<< HEAD
def eh_impar(numero):
    if numero % 2 != 0:
        return True
    return False
numero = int(input("Digite um numero para saber se ele é ímpar: "))

print(eh_impar(numero))
=======
def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

# Exemplo de uso:
n = int(input("Quantos termos da sequência de Fibonacci? "))
print(fibonacci(n))
>>>>>>> 356f9c7db0d01f814c9ef6c49e9c330222580ab6
