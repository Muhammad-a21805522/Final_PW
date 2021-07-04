from django.forms import ModelForm, ModelChoiceField
from .models import Contacto, Comentario, Quizz, ResultadoQuizz
from django import forms

CO2_Choices = [
    ('combustao', 'Carros a combustao'),
    ('eletricos', 'Carros eletricos'),
]
BestSeller_Choices = [
    ('tesla3', 'Tesla Model 3'),
    ('renaultZoe', 'Renault Zoe'),
    ('nissanL', 'Nissan Leaf'),
]

Battery_Choices = [
    ('tesla3', 'Tesla Model 3'),
    ('hyundaiK', 'Hyundai Kawai'),
    ('nissanL', 'Nissan Leaf'),
]

Horsepower_Choices = [
    ('1kw', '1 KW'),
    ('4kw', '4 KW'),
    ('075kw', '0.75 KW'),
]

Chargers_Choices = [
    ('1200', '1200'),
    ('802', '802'),
    ('1505', '1505'),
]

Charging_Choices = [
    ('20min', '20 minutos'),
    ('30min', '30 minutos'),
    ('60min', '60 minutos')
]

Cars_Choices = [
    ('teslas', 'Tesla Model S'),
    ('teslax', 'Tesla Model X'),
    ('porsche', 'Porsche Taycan'),
]
Cars2_Choices = [
    ('combustao', 'Carros a Combustão'),
    ('eletricos', 'Carros Elétricos'),
    ('hybrid', 'Carros Hibridos'),
    ('hybridPlug', 'Carros Hibridos Plug In'),
]


class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1...'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jota...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'JP@sublime.pt...'}),
            'apelido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pereira...'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '911524513...'}),
            'dataNascimento': forms.DateInput(),
        }


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'

        widgets = {
            'clareza': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1...'}),
            'rigor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1...'}),
            'precisao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1...'}),
            'profundidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1...'}),
            'amplitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1...'}),
            'logica': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1...'}),
            'significancia': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1...'}),
            'originalidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1...'}),
        }


class ResultadoForms(ModelForm):
    class Meta:
        model = ResultadoQuizz
        fields = '__all__'


class QuizzForms(forms.Form):
    question_CO2 = forms.CharField(label='Qual destes carros produz mais C02', widget=forms.Select(choices=CO2_Choices,))
    question_bestseller = forms.CharField(label='Qual o carro elétrico mais vendido',
                                          widget=forms.Select(choices=BestSeller_Choices))
    question_battery = forms.CharField(label='Qual destes carros tem maior autonomia',
                                       widget=forms.Select(choices=Battery_Choices))
    question_horsepower = forms.CharField(label='1 cavalo equivale a quantos KW',
                                          widget=forms.Select(choices=Horsepower_Choices))
    question_acce = forms.CharField(label='Qual é o carro que tem menor emissão de CO2',
                                    widget=forms.Select(choices=CO2_Choices))
    question_chargers = forms.CharField(label='Quantos pontos de carregamento existem em Lisboa? (Junho/2021)',
                                        widget=forms.Select(choices=Chargers_Choices))
    question_maintenance = forms.CharField(label='Qual destes carros necessita de menor manutenção',
                                           widget=forms.Select(choices=CO2_Choices))
    question_charging = forms.CharField(label='Qual o tempo médio de um carregamento ao utilizar um SuperCharger:',
                                        widget=forms.Select(choices=Charging_Choices))
    question_auto = forms.CharField(label='Qual o carro com maior autonomia?',
                                    widget=forms.Select(choices=Cars_Choices))
    question_eff = forms.CharField(label='Qual o tipo de carro com maior eficiência ?',
                                   widget=forms.Select(choices=Cars2_Choices))
