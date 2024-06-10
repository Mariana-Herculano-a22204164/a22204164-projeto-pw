from django.urls import path
from . import views

app_name = 'festivais'

urlpatterns = [
    path('', views.festival_list, name='lista_festivais'),
    path('<int:festival_id>/', views.festival_detail, name='detalhes_festival'),
]