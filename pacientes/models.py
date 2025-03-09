from django.db import models

# Create your models here.

class Pacientes(models.Model):
    queixa_choices = (
        ('TDAH','TRANSTORNO DE DEFICIT DE ATENÇÃO E HIPERATIVIDADE'),
        ('DEP','DEPRESSÃO'),
        ('ANS','ANSIEDADE')  ,
        ('TAG', 'TRANSTORNO DE ANSIEDADE GENERALIZADA')
    )
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=25, null=True, blank=True)
    foto = models.ImageField(upload_to='fotos')   #onde salvar a foto
    pagamento = models.BooleanField(default=True)
    queixa = models.CharField(max_length=6,choices=queixa_choices)
    
    
    def __str__(self):
        return self.nome