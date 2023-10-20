from django.db import models

from uploader.models import Image

class People(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=999)
    servico = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    idade = models.DecimalField(max_digits=3, decimal_places=0)
    valor = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    foto = models.ForeignKey(Image, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.nome} ({self.descricao}) {self.servico} ({self.valor}) {self.foto}"
    
    def first_image(self):
        return self.imagem.all()[0].url