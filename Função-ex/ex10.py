<<<<<<< HEAD
def area_circulo():
    raio = float(input("Digite o valor do raio do círculo: "))

    soma = (raio ** 2) * 3.14
    return soma

resultado = area_circulo()
print(f"A area do círculo é", resultado)
=======
numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

numero = int(input("Digite um número de 1 a 100: "))


if numero in numeros_primos:
    print("Seu número é primo")
    exit()

else:    
    print("Seu número não é primo")
    exit()
>>>>>>> 356f9c7db0d01f814c9ef6c49e9c330222580ab6
