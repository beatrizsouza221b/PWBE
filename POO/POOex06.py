class Aluno:
    def __init__(self, nome_aluno, curso, nota_final):
        self.nome_aluno = nome_aluno
        self.curso = curso
        self.nota_final = nota_final

    def status(self):
        print(f"Aluno {self.nome_aluno}\nCurso: {self.curso}\nNota: {self.nota_final}")

    def nota(self):
        if  self.nota_final > 7:
            return "Aprovado"
        return "Reprovado"
    
aluno_1 = Aluno("Ana", "Desenvolvimento de Sistemas", 10)
aluno_1.status()
print(aluno_1.nota())
        