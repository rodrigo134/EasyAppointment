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
    
    
class Tarefas(models.Model):
    frequencia_choices = (
        ('D', 'Diário'),
        ('1S', '1 vez por semana'),
        ('2S', '2 vezes por semana'),
        ('3S', '3 vezes por semana'),
        ('N', 'Ao necessitar')
    )
    tarefa = models.CharField(max_length=255)
    instrucoes = models.TextField()
    frequencia = models.CharField(max_length=2, choices=frequencia_choices, default='D')

    def __str__(self):
        return self.tarefa
    
    
    
class Consultas(models.Model):
    humor = models.PositiveIntegerField()
    registro_geral = models.TextField()
    video = models.FileField(upload_to="video")
    tarefas = models.ManyToManyField(Tarefas)  #relação N:N
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE) #chave estrangeira ,relação 1:N, on_delete = se paciente for excluido, consulta é excluida
    data = models.DateTimeField(auto_now_add=True) #auto_now_Add adicionar data da consulta

    def __str__(self):
        return self.paciente.nome