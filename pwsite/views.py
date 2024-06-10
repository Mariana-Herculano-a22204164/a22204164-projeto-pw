
# Create your views here.
# pwsite/views.py

from django.shortcuts import render
import datetime

def index_view(request):

    data = datetime.datetime.now().date()
    context = {'data': data }
    return render(request, "pwsite/index.html", context)


def sobre_view(request):
    return render(request, "pwsite/sobre.html")

def interesses_view(request):
    return render(request, "pwsite/interesses.html")