from django.db import models

class livro(models.Model):
    isbn = models.IntegerField(max_length = 20)
    nome = models.CharField(max_length = 255)
    descricao = models.CharField(max_length = 255)

    def __str__(self):
        return f"{self.isbn}\n{self.nome}\n{self.descricao}"

class categoria(models.Model):
    categoria = models.CharField(max_length= 255)

    def __str__(self):
        return f"{self.categoria}"

class autor(models.Model):
    nome_autor = models.CharField(max_length = 100)
    data_nasc = models.DateField(max_length = 20)
    biografia = models.TextField(max_length = 255)

    def __str__(self):
        return f"{self.nome_autor}\n{self.data_nasc}\n{self.biografia}"

class usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    data_cadastro = models.DateField(max_length=20)
    nivel = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.nome}\n{self.email}\n{self.data_cadastro}\n{self.nivel}"
    
class livro_categoria(models.Model):
    id_livro = models.ForeignKey(livro, on_delete = models.CASCADE)
    id_categoria = models.ForeignKey(categoria, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.id_livro}\n{self.id_categoria}"
    
class livro_autor(models.Model):
    id_autor = models.ForeignKey(autor, on_delete = models.CASCADE)
    id_livro = models.ForeignKey(livro, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.id_autor}\n{self.id_livro}"
    
class emprestimo(models.Model):
    id_usuario = models.ForeignKey(usuario, on_delete = models.CASCADE)
    id_livro = models.ForeignKey(livro, on_delete = models.CASCADE)
    data_emprestimo = models.DateField(max_length=20)
    devolucao_limite = models.DateField(max_length=20)
    data_devolucao = models.DateField(max_length = 20)
