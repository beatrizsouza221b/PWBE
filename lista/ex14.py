def fibonacci(n):
    sequencia = []
    a, b = 0, 1
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia

# Exemplo de uso:
n = int(input("Quantos termos da sequência de Fibonacci? "))
print(fibonacci(n))