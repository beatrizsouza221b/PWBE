from django.contrib import admin
from .models import livro
from .models import categoria
from .models import usuario
from .models import autor
from .models import livro_categoria
from .models import livro_autor
from .models import emprestimo

admin.site.register(livro)
admin.site.register(categoria)
admin.site.register(usuario)
admin.site.register(autor)
admin.site.register(livro_categoria)
admin.site.register(livro_autor)
admin.site.register(emprestimo)
# Register your models here.
