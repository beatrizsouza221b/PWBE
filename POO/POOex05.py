class Treinamento:
    def __init__(self, titulo, instrutor, duracao):
        self.titulo = titulo
        self.instutor  = instrutor
        self.duracao = duracao

    def descricao(self):
        print(f"O curso {self.titulo}, do instrutor {self.instutor} tem {self.duracao} de duração.")

treinamento_1 = Treinamento("Inteligencia Artificial", "Dorival", "5h")
treinamento_1.descricao()