from django.shortcuts import render, get_object_or_404
from .models import Festival

def festival_list(request):
    festivais = Festival.objects.all()
    return render(request, 'festivais/festival_list.html', {'festivais': festivais})

def festival_detail(request, festival_id):
    festival = get_object_or_404(Festival, id=festival_id)
    return render(request, 'festivais/festival_detail.html', {'festival': festival})