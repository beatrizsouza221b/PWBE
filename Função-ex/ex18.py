notas = [100, 50, 20, 10, 5, 2, 1]

valor = int(input("Digite um valor: "))

for nota in notas:
    quantidade = valor // nota
    if quantidade > 0:
        print(f"{quantidade} nota(s) de R$ {nota},00")
    valor %= nota
