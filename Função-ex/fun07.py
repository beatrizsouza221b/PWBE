def volume_cilindro():
    multiplicação = (raio ** 2) * 3.14
    volume = multiplicação * altura

    return volume

raio = int(input("Digite raio do cilindro: "))
altura = int(input("Digite altura do cilindro: "))

resultado = volume_cilindro()
print(f"O volume do cilindro é", resultado)
