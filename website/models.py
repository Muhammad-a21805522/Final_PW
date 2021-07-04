from django.db import models

# Create your models here.
from django.forms import ModelForm


class Contacto(models.Model):
    email = models.EmailField(max_length=254)
    nome = models.CharField(max_length=30)
    apelido = models.CharField(max_length=30)
    telefone = models.IntegerField(default=911524513)
    dataNascimento = models.DateField(default='2000-12-14')

    def __str__(self):
        return self.nome[:50]


class Comentario(models.Model):
    clareza = models.IntegerField(default=50)
    rigor = models.IntegerField(default=50)
    precisao = models.IntegerField(default=50)
    profundidade = models.IntegerField(default=50)
    amplitude = models.IntegerField(default=50)
    logica = models.IntegerField(default=50)
    significancia = models.IntegerField(default=50)
    originalidade = models.IntegerField(default=50)


class Quizz(models.Model):
    question_CO2 = models.CharField(max_length=30, default=1)
    question_bestseller = models.CharField(max_length=30, default=1)
    question_battery = models.CharField(max_length=30, default=1)
    question_horsepower = models.CharField(max_length=30, default=1)
    question_acce = models.CharField(max_length=30, default=1)
    question_chargers = models.CharField(max_length=30, default=1)
    question_maintenance = models.CharField(max_length=30, default=1)
    question_charging = models.CharField(max_length=30, default=1)
    question_auto = models.CharField(max_length=30, default=1)
    question_eff = models.CharField(max_length=30, default=1)
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE, default=1)

class ResultadoQuizz(models.Model):
    resultado = models.IntegerField(default=0)


class Quizzform(ModelForm):
    class Meta:
        model = Quizz
        fields = ['question_CO2', 'question_bestseller', 'question_battery', 'question_horsepower', 'question_acce',
                  'question_chargers', 'question_maintenance', 'question_charging', 'question_auto', 'question_eff']
