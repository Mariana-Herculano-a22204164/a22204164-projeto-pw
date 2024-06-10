from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import requests


def weather_today_lisbon(request):
    url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        forecast = weather_data['data'][0]

        weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'
        weather_types_response = requests.get(weather_types_url)
        if weather_types_response.status_code == 200:
            weather_types = weather_types_response.json()
            weather_type = next((wt for wt in weather_types['data']
                                if wt['idWeatherType'] == forecast['idWeatherType']), None)
            weather_description = weather_type['descWeatherTypePT'] if weather_type else 'Unknown'

            context = {
                'city': 'Lisboa',
                'min_temp': forecast['tMin'],
                'max_temp': forecast['tMax'],
                'date': forecast['forecastDate'],
                'weather_description': weather_description,
                'id_weather_type': forecast['idWeatherType']
            }
            return render(request, 'meteo/weather_today.html', context)
    return render(request, 'meteo/weather_today.html', {'error': 'Could not fetch weather data'})


def weather_next_5_days(request):
    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    cities_response = requests.get(cities_url)
    cities = cities_response.json() if cities_response.status_code == 200 else []
    cities = cities['data']
    selected_city = request.GET.get('city')
    forecast_data = []

    if selected_city:
        city_id = next((city['globalIdLocal'] for city in cities if city['local'] == selected_city), None)
        if city_id:
            forecast_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
            forecast_response = requests.get(forecast_url)
            if forecast_response.status_code == 200:
                forecast_data = forecast_response.json().get('data', [])
    weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'
    weather_types_response = requests.get(weather_types_url)
    if weather_types_response.status_code == 200:
        weather_types = weather_types_response.json()
    else:
        weather_types = ["N/A" for _ in range(100)]
    weather_types = weather_types['data']
    weather_types = {w['idWeatherType']:w['descWeatherTypePT'] for w in weather_types}
    context = {
        'cities': cities,
        'selected_city': selected_city,
        'forecast_data': forecast_data,
        'weather_types': weather_types
    }
    return render(request, 'meteo/weather_next_5_days.html', context)


def api_list_cities(_request):
    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    cities_response = requests.get(cities_url)
    cities = cities_response.json() if cities_response.status_code == 200 else []
    return JsonResponse(cities, safe=False)


def api_weather_today(_request, city_id):
    forecast_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    forecast_response = requests.get(forecast_url)
    forecast_data = forecast_response.json().get('data', [])[0] if forecast_response.status_code == 200 else {}
    return JsonResponse(forecast_data)


def api_weather_next_5_days(_request, city_id):
    forecast_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    forecast_response = requests.get(forecast_url)
    forecast_data = forecast_response.json().get('data', []) if forecast_response.status_code == 200 else []
    return JsonResponse(forecast_data, safe=False)

def api_description(request):
    return render(request, 'meteo/api_description.html')