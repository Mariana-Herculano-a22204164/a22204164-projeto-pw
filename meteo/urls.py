from django.urls import path
from .import views

app_name = "meteo"

urlpatterns = [
    path('weather/today/lisbon/', views.weather_today_lisbon, name='weather_today_lisbon'),
    path('weather/next-5-days/', views.weather_next_5_days, name='weather_next_5_days'),
    path('api/cities/', views.api_list_cities, name='api_list_cities'),
    path('api/weather/today/<int:city_id>/', views.api_weather_today, name='api_weather_today'),
    path('api/weather/next-5-days/<int:city_id>/', views.api_weather_next_5_days, name='api_weather_next_5_days'),
    path('api/description/', views.api_description, name='api_description'),
]
