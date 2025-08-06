list = []

for i in range(5):
    numeros = int(input(f"Digite um número {i + 1}: "))
    list.append(numeros)

print(f"O maior número da lista é {max(list)}\nO menor número da lista é {min(list)}")
