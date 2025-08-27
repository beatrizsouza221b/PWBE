class Pessoa:
    def __init__(self, nome, idade, setor):
        self.nome = nome
        self.idade = idade
        self.setor = setor

    def apresentar(self):
        print(f"Essas são as informações sobre essa pessoa:\nNome: {self.nome}\nIdade: {self.idade}\nSetor: {self.setor}")

pessoa_1 = Pessoa("Ana", 19, "Engenharia")
pessoa_1.apresentar()