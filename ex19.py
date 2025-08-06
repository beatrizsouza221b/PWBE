palavra = input("Digite uma palavra: ")

invertida = palavra[::-1]
print(f"A palavra invertida é: {invertida}")

if invertida == palavra:
    print("A palavra é um palíndromo.")

else:
    print("Essa palavra não é um palíndromo")
