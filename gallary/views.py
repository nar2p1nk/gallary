from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .models import Profiles
from django.views.generic import ListView,CreateView,DetailView
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

class Detail(DetailView):
    model=Profiles
    template_name = 'detail.html'



