from django.shortcuts import render
import requests
from django.views import View
import json
import socket
# Create your views here.
class home(View):
    def get(self,request):
        send_url = 'https://jsonplaceholder.typicode.com/posts/'
        r = requests.get(send_url)
        j = json.loads(r.text)
        return render(request,'geo/home.html',{
            'obj':j
        })
class location(View):
    def get(self,request):
        hostname=socket.gethostname()
        ip_add='47.247.144.96'
        print(ip_add)
        params = {'access_key':'88e036d1c9410193b8b11bd811dc9687'}
        response=requests.get(url=f'http://api.ipstack.com/{ip_add}',params=params)
        geodata = response.json()
        return render(request, 'geo/map.html', {
            'text':response.json()
        })