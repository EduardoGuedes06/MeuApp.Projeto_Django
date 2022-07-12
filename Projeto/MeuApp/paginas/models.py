from django.db import models

# Create your models here.
class Produto(models.Model):
    id_produto = models.ForeignKey(on_delete=models.CASCADE)
    produto_nome = models.CharField(max_length=30)
    produto_descricao = models.CharField(max_length=30)
    produto_preco = models.int(max_length=30)