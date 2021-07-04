from django.contrib import admin
from .models import Contacto, Comentario, Quizz, ResultadoQuizz

# Register your models here.
admin.site.register(Contacto)
admin.site.register(Comentario)
admin.site.register(Quizz)
admin.site.register(ResultadoQuizz)