<<<<<<< HEAD
def area_quadrado():
    lado = float(input("Digite o valor do lado do quadrado: "))

    soma = lado ** 2
    return soma

resultado = area_quadrado()
print(f"A area do quadardo é", resultado)
=======
lista = []

nota = float(input("Digite uma nota ou digite '-1' para encerrar o programa: "))
lista.append(nota)

if nota == -1:
    print("Programa encerrado")
    exit()

else:
    while True:
        notas = float(input("Digite outra nota ou digite '-1' para encerrar o programa: "))

        if notas != -1:
            lista.append(notas)

        else:
            media = sum(lista) / len(lista)
            print(f"Você adicionou as notas: {lista}\nA média das suas notas é {media}")
            break
>>>>>>> 356f9c7db0d01f814c9ef6c49e9c330222580ab6
