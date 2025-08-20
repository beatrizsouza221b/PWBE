<<<<<<< HEAD
#decimal para binario
def decimal_para_binario(numero):
    binario = ""
    while numero > 0:              #enquanto o numero for maior que zero a conta continua
        resto = numero % 2         #resto é igual ao resto da dvisão do numero por 2
        binario = str(resto) + binario    # 
        numero = numero // 2      # // descarta o resto 
    return binario

numero = int(input("Digite um número para trnsformá-lo em binário: "))
numero_binario = decimal_para_binario(numero)
print(f"O número decimal {numero} em binário é: {numero_binario}")
=======
for i in range(11):
    print(i)
>>>>>>> 356f9c7db0d01f814c9ef6c49e9c330222580ab6
