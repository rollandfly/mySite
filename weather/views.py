from django.shortcuts import render
import requests
# Create your views here.
def weatherPage(request):
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=64b431b4e7251052ae95104f0f507716'
  city="Las Vegas"
  r = requests.get(url.format(city)).json()

  city_weather = {
    'city': city,
    'temperature': r['main']['temp'],
    'description': r['weather'][0]['description'],
    'icon':r['weather'][0]['icon'],
  }

  print(city_weather)
  context = {'city_weather':city_weather}

  return render(request,'weather/weather.html',context)