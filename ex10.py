numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

numero = int(input("Digite um número de 1 a 100: "))


if numero in numeros_primos:
    print("Seu número é primo")
    exit()

else:    
    print("Seu número não é primo")
    exit()