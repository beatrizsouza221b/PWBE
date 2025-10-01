num = int(input("Digite um número inteiro: "))
if num == 0:
    binario = "0"
else:
    binario = ""
    n = num
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2
print(f"O número {num} em binário é: {binario}")