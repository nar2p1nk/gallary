from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Profiles
from django.views.generic import ListView,CreateView
#from django.http import HttpResponseRedirect
from .forms import PostForm,PostForm2
from django.urls import reverse_lazy
#from django.views.generic.edit import FormView
# Create your views here.


class Display(ListView):
    model=Profiles
    template_name = 'dex.html'

class send(CreateView):
    model = Profiles
    form_class = PostForm2
    template_name = 'form.html'
    success_url = reverse_lazy('home')

def home(request):
    return render(request, 'home.html',{})

# homepage1 | homepage2
#     1            2