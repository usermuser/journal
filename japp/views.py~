# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView 
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import ListView, DetailView
from .models import Pda

class PdaChangesListView(ListView):
    template_name = ('japp/list.html')
    context_object_name = 'latest_pda_changes'

    def get_queryset(self):
        return Pda.objects.order_by('-date')
    
class PdaChangesDetailView(DetailView):
    model = Pda
    template_name = ('japp/detail.html')


class PdaChangesRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'japp/register.html'
    success_url = reverse_lazy('japp:index')

class PdaChangesCreateView(CreateView):
    model = Pda
    template_name = 'japp/add.html'
    fields = ['text','cpu']
    success_url = reverse_lazy('japp:index')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PdaChangesCreateView, self).form_valid(form)
