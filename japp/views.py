# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView 
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import ListView, DetailView
from .models import Pda

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

'''
def listing(request):
    pda_changes_list =Pda.objects.order_by('-user')
    paginator = Paginator(pda_changes_list,5) # Show 25 contacts per page
    page = request.GET.get('page')
    
    try:
        pda_changes= paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pda_changes= paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pda_changes= paginator.page(paginator.num_pages)

    return render(request, 'japp/test.html', {'pda_changes': pda_changes})
'''

def listing_by_date(request):
    pda_changes_list =Pda.objects.order_by('-date')
    paginator = Paginator(pda_changes_list,20) # Show 10 contacts per page
    page = request.GET.get('page')
    
    try:
        pda_changes= paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pda_changes= paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pda_changes= paginator.page(paginator.num_pages)

    return render(request, 'japp/test.html', {'pda_changes': pda_changes})



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

