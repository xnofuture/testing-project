import re
from django.shortcuts import render
from django.http import HttpResponse
from dadata import Dadata

# Create your views here.
def home(request):
    return render(request, 'yesdata/main.html')



def get_adress(request):
    token = "7e9cd4acd7cca5b091ac0807e21a626a580c95ec"
    dadata = Dadata(token)
    data = request.GET.get('address')
    results = dadata.suggest(name="address", query=data)[0]
    keywords = ["postal_code", "region", "fias_id", "fias_code", "geo_lat", "geo_lon"]
    descriptions = [results['data'][i] for i in results['data'] if i in keywords] 
    return render(request, 'yesdata/get_adress.html', {'data': descriptions, 'adres': data})

