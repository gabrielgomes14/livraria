from django.db import models
from django.core.exceptions import ValidationError
from .categoria import Categoria
from .editora import Editora
from .autor import Autor
from uploader.models import Image
from .livro import Livro

def validate_avaliacao(value):
    if value > 10:
        raise ValidationError('A avaliação não pode ser maior que 10.')

class Favorito(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    avaliacao = models.IntegerField(validators=[validate_avaliacao])
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="favoritos", null=True, blank=True)
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="favoritos", null=True, blank=True)
    autor = models.ManyToManyField(Autor, related_name="favoritos", blank=True)
    comentarios = models.TextField(null=True, blank=True)  # Campo de texto para comentários

    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"({self.id}) {self.titulo} ({self.avaliacao})"
