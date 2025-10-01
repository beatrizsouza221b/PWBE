list = []

for i in range(5):
    nota = float(input(f"Digite suas notas {i + 1}: "))
    list.append(nota)

media = sum(list) / len(list)
print(f"Sua média é {media}")

if media >= 5:
    print("Aprovado")

elif media >= 2.5 and media < 5:
    print("Recuperação")

else:
    print("Reprovado")