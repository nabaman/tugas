from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from geopy import Nominatim

@api_view(['POST'])
def get_api(request):
    loc_name = request.data.get('loc_name')
    if loc_name == '':
        return Response('Error', status=400)
    geolocator = Nominatim(user_agent="myAgent")
    location = geolocator.geocode(loc_name)
    return Response(f'latitude : {location.latitude} , longitude : {location.longitude}', status=200)
