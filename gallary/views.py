from django.shortcuts import render
from .models import Profiles
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .forms import PostForm
# Create your views here.


class Display(ListView):
    model=Profiles
    template_name='dex.html'

def send(request):

    if request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_valid():

            return HttpResponseRedirect('home/')

    else:

        form = PostForm()


    return render(request,'form.html',{'form':form})




