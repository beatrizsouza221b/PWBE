<<<<<<< HEAD
def volume_cilindro():
    multiplicação = (raio ** 2) * 3.14
    volume = multiplicação * altura

    return volume

raio = int(input("Digite raio do cilindro: "))
altura = int(input("Digite altura do cilindro: "))

resultado = volume_cilindro()
print(f"O volume do cilindro é", resultado)
=======
list = []

for i in range(5):
    numeros = int(input(f"Digite um número {i + 1}: "))
    list.append(numeros)

print(f"O maior número da lista é {max(list)}\nO menor número da lista é {min(list)}")
>>>>>>> 356f9c7db0d01f814c9ef6c49e9c330222580ab6
