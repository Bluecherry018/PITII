from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse





class Entry(models.Model):
    Mood = [
        ('\U0001F600', '\U0001F600 Feliz'),
        ('\U0001F610', '\U0001F610 Indiferente'),
        ('\U0001F61E', '\U0001F61E Triste'),
        ('\U0001F621', '\U0001F621 Bravo'),
        ('\U0001F62B', '\U0001F62B Cansado'),
        ('\U0001F624','\U0001F624 Estressado'),
    ]
  
    Qualidade = [
        ('\U0001F634', '\U0001F634 Bom'),
        ('\U0001F971', '\U0001F971 Insônia'),
        ('\U0001F62B', '\U0001F62B Ruim'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='entries')



   
    title = models.CharField(default='\U0001F600 Bom',max_length=1, choices=Mood, verbose_name='Humor')
    content = models.TextField(verbose_name='Descreva o seu dia')
    date_created = models.DateTimeField(default=timezone.now)

   
    remedios = models.ManyToManyField('Remedio', related_name='entries')


    sono = models.CharField(default='\U0001F634 Bom',max_length=100, choices=Qualidade, verbose_name='Qualidade do Sono')
    horas = models.PositiveIntegerField(default='',verbose_name='Quantas horas de Sono')
    informe = models.TextField(default='',verbose_name='Descreva o seu sono')




    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Entries"

    def get_absolute_url(self):
        return reverse('entry-detail', args=[str(self.id)])

class Remedio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    nome = models.CharField(max_length=100, verbose_name='Nome e Dosagem')
    descricao = models.TimeField(verbose_name='Horário')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
    
class Planner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pequeno_almoco = models.CharField(max_length=255, blank=True)
    almoco = models.CharField(max_length=255, blank=True)
    lanche = models.CharField(max_length=255, blank=True)
    jantar = models.CharField(max_length=255, blank=True)
    prioridades = models.TextField(blank=True)
    compromissos = models.TextField(blank=True)
    tarefas = models.TextField(blank=True)
    coisas_para_comprar = models.TextField(blank=True)
    limpar_a_casa = models.TextField(blank=True)
    lema = models.CharField(max_length=255, blank=True)
    anotacoes = models.TextField(blank=True)
    copos_agua = models.PositiveIntegerField(default=0)  

    compromissos1 = models.TextField(blank=True)
    compromissos2 = models.TextField(blank=True)
    compromissos3 = models.TextField(blank=True)
    compromissos4 = models.TextField(blank=True)
    compromissos5 = models.TextField(blank=True)
    compromissos6 = models.TextField(blank=True)

    prioridade1 = models.TextField(blank=True)
    prioridade2 = models.TextField(blank=True)
    prioridade3 = models.TextField(blank=True)
    prioridade4 = models.TextField(blank=True)
    prioridade5 = models.TextField(blank=True)
    prioridade6 = models.TextField(blank=True)

    compras1 = models.TextField(blank=True)
    compras2 = models.TextField(blank=True)
    compras3 = models.TextField(blank=True)
    compras4 = models.TextField(blank=True)
    compras5 = models.TextField(blank=True)
    compras6 = models.TextField(blank=True)


    fazer1 = models.TextField(blank=True)
    fazer2 = models.TextField(blank=True)
    fazer3 = models.TextField(blank=True)
    fazer4 = models.TextField(blank=True)
    fazer5 = models.TextField(blank=True)
    fazer6 = models.TextField(blank=True)

    limpar1 = models.TextField(blank=True)
    limpar2 = models.TextField(blank=True)
    limpar3 = models.TextField(blank=True)
    limpar4 = models.TextField(blank=True)
    limpar5 = models.TextField(blank=True)
    limpar6 = models.TextField(blank=True)

    def __str__(self):
        return f"Planner de {self.user.username}"
    
