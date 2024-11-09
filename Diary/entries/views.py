from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
import json
from datetime import timedelta, timezone
import requests

from django.utils import timezone
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,

)
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Remedio
from .forms import RemedioForm
from django.http import JsonResponse
from django.core.cache import cache
import requests
import datetime




from .models import Entry, Remedio,Planner
class LockedView(LoginRequiredMixin):
    login_url = "admin:login"

class EntryListView(LockedView, ListView):
    model = Entry
    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user).order_by("-date_created")
    

class EntryDetailView(LockedView, DetailView):
    model = Entry

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entry = self.get_object()
        context['remedios'] = entry.remedios.all()
        context['registros'] = Entry.objects.values('sono', 'horas', 'informe')  
        return context

class EntryCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "content", "sono", "horas", "informe"]  
    success_url = reverse_lazy("entry-list")
    success_message = "Seu registro foi criado!"

    def form_valid(self, form):
        form.instance.user = self.request.user  
        response = super().form_valid(form)
        form.instance.remedios.set(self.request.POST.getlist('remedios'))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['remedios'] = Remedio.objects.filter(user=self.request.user)

        context['registros'] = Entry.objects.filter(user=self.request.user).values('sono', 'horas', 'informe')

        return context

class EntryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "content", "sono", "horas", "informe"]
    success_message = "Registro atualizado!"


    def get_success_url(self):
        return reverse_lazy("entry-detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user  
        response = super().form_valid(form)
        form.instance.remedios.set(self.request.POST.getlist('remedios'))
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['remedios'] = Remedio.objects.all()
        context['remedios'] = Remedio.objects.filter(user=self.request.user)

        # context['registros'] = Entry.objects.values('sono', 'horas', 'informe', 'date_created')   # Passando os remédios para o template
        context['registros'] = Entry.objects.filter(user=self.request.user).values('sono', 'horas', 'informe')


        return context

class EntryDeleteView(LockedView, SuccessMessageMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Registro deletado!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

class LockedView(LoginRequiredMixin):
    login_url = "admin:login"


class RemedioListView(LockedView, ListView):
    model = Remedio
    template_name = "entries/remedio_list.html" 

    def get_queryset(self):
        return Remedio.objects.filter(user=self.request.user).order_by("-data_criacao")

class RemedioDetailView(LockedView, DetailView):
    model = Remedio

class RemedioCreateView(CreateView):
    model = Remedio
    form_class = RemedioForm
    template_name = "entries/remedio_form.html"  # Substitua pelo seu template
    success_url = reverse_lazy("remedio-list")

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class RemedioUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Remedio
    form_class = RemedioForm
    success_message = "O remédio foi atualizado com sucesso!"
    template_name = "entries/remedio_form.html"  # Defina o template se necessário

    def get_queryset(self):
        # Filtra apenas os remédios do usuário atual para atualização
        return Remedio.objects.filter(user=self.request.user)

    def get_success_url(self):
        # Define o redirecionamento após a atualização
        return reverse_lazy("remedio-detail", kwargs={"pk": self.object.pk})

class RemedioDeleteView(LockedView, SuccessMessageMixin, DeleteView):
    model = Remedio
    success_url = reverse_lazy("remedio-list")
    success_message = "O remédio foi excluído com sucesso!"

    def get_queryset(self):
        return Remedio.objects.filter(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
    

class SonoRegistroListView(ListView):
    model = Entry
    template_name = "entries/sono_registro_list.html"
    context_object_name = "registros"

   
    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user).order_by("-date_created")

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        registros = context['registros']

        # Filtrar apenas os registros do mês atual
        agora = timezone.now()
        inicio_mes_atual = agora.replace(day=1)
        registros_mes_atual = [r for r in registros if r.date_created >= inicio_mes_atual]

        # Calcular a média de horas dormidas no mês atual
        if registros_mes_atual:
            total_horas_mes = sum(r.horas for r in registros_mes_atual)
            media_horas_mes = total_horas_mes / len(registros_mes_atual)
        else:
            media_horas_mes = 0

        horas_dormidas = [r.horas for r in registros_mes_atual]
        datas_registros = [r.date_created.strftime('%d/%m/%Y') for r in registros_mes_atual]

        context['horas_dormidas'] = horas_dormidas
        context['datas_registros'] = datas_registros
        context['media_horas'] = [media_horas_mes]  # Passa a média como lista para o template
        return context

class SonoDetailView(LockedView, DetailView):

    model = Entry
    template_name = "entries/sono_detail.html"
    context_object_name = "entry"

    def get_success_url(self):
        return reverse_lazy("sono-detail", kwargs={"pk": self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entry = self.get_object()
        context['registros'] = Entry.objects.filter(user=self.request.user).values('sono', 'horas', 'informe')

        return context
    

class CalendarView(TemplateView):
    template_name = 'entries/calendario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entries =  Entry.objects.filter(user=self.request.user)

        # Definindo as cores de acordo com o humor (title)
        color_map = {
            "\U0001F600": '#69c67c',    
            "\U0001F610": '#a49180',   
            "\U0001F61E": '#5589c4',      
            "\U0001F621": '#d92d37',
            "\U0001F62B": '#8d6cc3',
            "\U0001F624": '#e8533e'
        }

        events = []
        for entry in entries:
            color = color_map.get(entry.title, 'gray')  # Cor padrão é cinza se o humor não for encontrado
            events.append({
                'title': entry.get_title_display(),  # Exibe o humor completo
                'start': timezone.localtime(entry.date_created).strftime('%Y-%m-%d'),
                'color': color,
                'url': self.request.build_absolute_uri(entry.get_absolute_url())
            })

        context['events'] = json.dumps(events)
        return context
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após o registro
    else:
        form = UserCreationForm()
    return render(request, 'entries/register.html', {'form': form})


def get_random_quote():
    # Tenta recuperar a frase do dia do cache
    quote_of_the_day = cache.get('quote_of_the_day')
    today = datetime.date.today()

    # Se não houver frase armazenada para o dia, gera uma nova
    if not quote_of_the_day or quote_of_the_day['date'] != today:
        url = "https://api.quotable.io/random"
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            data = response.json()
            quote = data.get('content', 'Frase não disponível.')
            author = data.get('author', 'Desconhecido')
            quote_of_the_day = {
                'quote': f'"{quote}" - {author}',
                'date': today
            }
            # Armazena a frase no cache por 24 horas
            cache.set('quote_of_the_day', quote_of_the_day, 60 * 60 * 24)
        else:
            quote_of_the_day = {'quote': "Frase do dia não disponível no momento.", 'date': today}

    return quote_of_the_day['quote']



@login_required
def home(request):
    planner, created = Planner.objects.get_or_create(user=request.user)
    quote_of_the_day = get_random_quote()

    if request.method == 'POST':
        field_name = request.POST.get('name')
        field_value = request.POST.get('value')
        

        if 'clear_all' in request.POST:
            # Zera todos os campos do planner
            fields_to_clear = [
                'pequeno_almoco', 'almoco', 'lanche', 'jantar', 'copos_agua',
                'prioridade1', 'prioridade2', 'prioridade3', 'prioridade4', 'prioridade5', 'prioridade6',
                'limpar1', 'limpar2', 'limpar3', 'limpar4', 'limpar5', 'limpar6',
                'fazer1', 'fazer2', 'fazer3', 'fazer4', 'fazer5', 'fazer6',
                'compras1', 'compras2', 'compras3', 'compras4', 'compras5', 'compras6',
                'lema', 'anotacoes', 'compromissos1', 'compromissos2', 'compromissos3', 'compromissos4', 'compromissos5', 'compromissos6',
            ]
            for field in fields_to_clear:
                setattr(planner, field, "")
            planner.copos_agua = 0
            planner.save()
            return redirect('home')

        # Ação para adicionar ou remover copos de água
        if 'add_copo' in request.POST:
            planner.copos_agua += 1
            planner.save()

        elif 'remove_copo' in request.POST and planner.copos_agua > 0:
            planner.copos_agua -= 1
            planner.save()

        if field_name and hasattr(planner, field_name):
            setattr(planner, field_name, field_value)
            planner.save()


    # Gera a lista de prioridades, preenchendo com campos vazios se necessário
    prioridades = [getattr(planner, f'prioridade{i}', '') for i in range(1, 7) if getattr(planner, f'prioridade{i}', '')]
    limpeza = [getattr(planner, f'limpar{i}', '') for i in range(1, 7) if getattr(planner, f'limpar{i}', '')]
    fazer = [getattr(planner, f'fazer{i}', '') for i in range(1, 7) if getattr(planner, f'fazer{i}', '')]
    compras = [getattr(planner, f'compras{i}', '') for i in range(1, 7) if getattr(planner, f'compras{i}', '')]
    compromisso = [getattr(planner, f'compromissos{i}', '') for i in range(1, 7) if getattr(planner, f'compromissos{i}', '')]




    context = {
        'planner': planner,
        'username': request.user.username,
        'prioridades': prioridades,
        'limpeza': limpeza,
        'fazer': fazer,
        'compras': compras,
        'compromisso': compromisso,
        'quote_of_the_day': quote_of_the_day,
    }

    return render(request, 'entries/home.html', context)
