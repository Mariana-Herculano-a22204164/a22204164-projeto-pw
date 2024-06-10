from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about_page, name='about_page'),
    path('techtools/', views.techtools_page, name='techtools_page'),
]