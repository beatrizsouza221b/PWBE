
def media(lista):
    media = sum(lista) / 3
    print(media)
    return media

lista = []

for i in range (3):
    valor = int(input("Digite tres números e receba a média deles: "))
    lista.append(valor)

media(lista)
