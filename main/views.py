from django.shortcuts import render
from django.http import JsonResponse
import Adafruit_DHT
import socket

def index(request):
    return render(request, 'main/main.html', {'hostname': socket.gethostname()})

def api(request):
    sensor = Adafruit_DHT.DHT11
    pin = 4
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return JsonResponse({'Temp':temperature, 'Hum':humidity})
