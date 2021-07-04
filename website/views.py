from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
import datetime

from django.urls import reverse

from website.forms import ContactoForm, ComentarioForm, QuizzForms, ResultadoForms
from website.models import Contacto, Comentario, Quizzform, Quizz, ResultadoQuizz
from website.utils import get_plot, media, corrigir, get_plotv2


def home_page_view(request):
    lista = ["HTML", "CSS", "Python", "Django"]
    context = {
        'agora': datetime.datetime.now(),
        'lista': lista,
        'contactos': Contacto.objects.all(),
    }
    return render(request, 'website/base.html', context)


def multi_page_view(request):
    return render(request, 'website/multimedia.html')


def dif_page_view(request):
    return render(request, 'website/diferencas.html')


def amb_page_view(request):
    return render(request, 'website/ambiente.html')


def form_page_view(request):
    fields = ['question_CO2', 'question_bestseller', 'question_battery', 'question_horsepower', 'question_acce',
              'question_chargers', 'question_maintenance', 'question_charging', 'question_auto', 'question_eff']
    answers = []
    b = 0
    if request.method == 'POST':
        form = Quizzform(request.POST)
        if form.is_valid():
            form.save()
            for question in fields:
                answers.append(form.cleaned_data[question])
            request.session['answers'] = answers
            print(answers)
            nota = corrigir(answers)
            b = ResultadoQuizz(resultado=nota)
            b.save()
            notas = ResultadoQuizz.objects.all()
            x = ['Média de todos os Resultados']
            t = [t.resultado for t in notas]
            mediaNotas = media(t)
            chart = get_plotv2(x, mediaNotas)
            context = {'nota': b, 'chart': chart}
            return render(request, 'website/resultadoquizz.html', context)
    form = QuizzForms
    context = {"form": form, 'nota': b}
    return render(request, 'website/form.html', context)


def tecnicas_page_view(request):
    return render(request, 'website/tecnicas.html')


def inventario_page_view(request):
    return render(request, 'website/inventario.html')


def apresentacao_page_view(request):
    return render(request, 'website/video.html')


def intro_page_view(request):
    return render(request, 'website/index.html')


def contactos_page_view(request):
    context = {'contactos': Contacto.objects.all()}
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('website:login'))
    return render(request, 'website/contactos.html', context)


def nova_tarefa_view(request):
    form = ContactoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:contacto'))

    context = {'form': form}

    return render(request, 'website/addContacto.html', context)


def edita_tarefa_view(request, contacto_id):
    contacto = Contacto.objects.get(id=contacto_id)
    form = ContactoForm(request.POST or None, instance=contacto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:contacto'))

    context = {'form': form, 'contacto_id': contacto_id}
    return render(request, 'website/editContacto.html', context)


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('website:contacto'))
        else:
            return render(request, 'website/login.html', {
                'message': 'Credenciais inválidas.'
            })

    return render(request, 'website/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'website/login.html', {
        'message': 'Logged out'})


def apaga_tarefa_view(request, contacto_id):
    Contacto.objects.get(id=contacto_id).delete()
    return HttpResponseRedirect(reverse('website:contacto'))


def resultadoComentarios_page_view(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:comentarios'))
    context = {'form': form}
    return render(request, 'website/resultadocomentario.html', context)


def comentarios_page_view(request):
    qs = Comentario.objects.all()
    x = ["Clareza", "Rigor", "Precisao", "Profundidade", "Amplitude", "Logica", "Significancia", "Originalidade"]
    y3 = []
    y = [y.clareza for y in qs]
    y2 = media(y)
    y3.append(y2)
    y = [y.rigor for y in qs]
    y2 = media(y)
    y3.append(y2)
    y = [y.precisao for y in qs]
    y2 = media(y)
    y3.append(y2)
    y = [y.profundidade for y in qs]
    y2 = media(y)
    y3.append(y2)
    y = [y.amplitude for y in qs]
    y2 = media(y)
    y3.append(y2)
    y = [y.logica for y in qs]
    y2 = media(y)
    y3.append(y2)
    y = [y.significancia for y in qs]
    y2 = media(y)
    y3.append(y2)
    y = [y.originalidade for y in qs]
    y2 = media(y)
    y3.append(y2)
    chart = get_plot(x, y3)
    context = {'comentarios': Comentario.objects.all(), 'chart': chart}
    return render(request, 'website/comentario.html', context)


def resultadosQuizz_page_view(request):
    context = []
    return render(request, 'website/resultadoquizz.html', context)


def spa_page_view(request):
    return render(request, 'website/spa.html')


texts = ["O primeiro automóvel com motor de combustão foi criado em 1886 graças ao Engenheiro Mecânico Karl Benz.  "
         "Esse automóvel tinha uma potência de 0,75 cavalos e atingia uma velocidade máxima de 16 km/h",
         "Em 1913, com a execução da primeira linha de montagem por Henry Ford, o custo dos automóveis foi baixando o "
         "que permitiu a adopção deste meio de transporte por parte das massas",
         "Com a crescente preocupação da pegada ambiental, a tendência é adotar soluções 100% elétricas ","Website sobre os Automóveis Elétricos"]


def section_page_view(request, num):
    if 1 <= num <= 4:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No Such section")
