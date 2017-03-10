from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from clientlist.models import Clients

# Create your views here.
def clients(request):
    return render_to_response('clientlist.html', {'clients': Clients.objects.all()})

def client(request, clients_id=1):
    return render_to_response('client.html', {'client': Clients.objects.get(id=clients_id)})