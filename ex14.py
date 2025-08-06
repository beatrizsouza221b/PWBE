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