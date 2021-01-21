from django.shortcuts import render,HttpResponse
import requests

def dashboard_view(request):
    
    return render(request, 'dashboard.html')

def send_api(request):
    lat = request.POST.get('lat')
    long = request.POST.get('long')
    data = {
        'lat':lat,
        'long':long
    }
    r = requests.post('http://localhost:8001/api-2/',data=data)
    return HttpResponse(r.json())
