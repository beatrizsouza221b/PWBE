class Manual:
    def __init__(self, titulo,autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def informacoes(self):
        print(f"O manual {self.titulo}, escrito por {self.autor}, foi publicado em {self.ano_publicacao}")

manual_1 = Manual("Programação Back-End com Python", "Dorival", "20/07/2022")
manual_1.informacoes()