#binario para decimal

def binario_para_decimal(binario):
    numero = binario[::-1]
    potencia = 0
    soma = 0
    for i in numero:
        soma += int(i) * (2**potencia)
        potencia += 1
    
    return soma

binario = input("Digite um número binário: ")
print(binario_para_decimal(binario))