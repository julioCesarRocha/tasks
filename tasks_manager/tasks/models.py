from django.db import models

class Task(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    responsavel = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title