from django.shortcuts import render

def landing_page(request):
    return render(request, 'portfolio/landing_page.html')

def about_page(request):
    return render(request, 'portfolio/about.html')

def techtools_page(request):
    return render(request, 'portfolio/techtools.html')