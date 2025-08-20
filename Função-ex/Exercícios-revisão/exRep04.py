import random
print("Vamos jogar forca!\n")
print("Advinhe o país.\n")

paises = ["china", "brasil", "angola", "argentina", "venezuela"]
letras = []

palavra_secreta = random.choice(paises)

print(f"Sua palavra tem {len(palavra_secreta)} letras")
print(f"{"_ " * len(palavra_secreta)}")

#_ = [letra for letra in texto if letra.isalpha()]
while True:
    letra = input("Digite uma letra: ")

    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
             if palavra_secreta[i] == letra:
                #palavra_exibida[i] = letra
                letras_acertadas += 1
        #letras.append(letra)
        print(f"Você acertou uma letra, o país secreto tem as seguintes letras: {letras}")

        #palavra_exibida[index] = letra
    else:
        print(f"O país secreto não tem essa letra.\nContinue tentando!\nO país secreto tem as seguintes letras: {letras}")
