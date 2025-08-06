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