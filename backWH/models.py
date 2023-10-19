from django.db import models

from uploader.models import Image

class People(models.Model):
    name = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    servico = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    age = models.DecimalField(max_digits=3)
    valor = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        default=None,
    )

    def __str__(self):
        return f"{self.name} ({self.descricao}) {self.servico} ({self.valor}) {self.foto}"