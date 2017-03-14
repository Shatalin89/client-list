from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from clientlist.models import Clients
from django.template.loader import get_template
from clientlist.forms import ClientsForm
from django.template.context_processors import csrf
from django.shortcuts import redirect


# Create your views here.
def clients(request):
    return render_to_response('clientlist.html', {'clients': Clients.objects.all()})

def client(request, clients_id=1):
    args ={}
    args.update(csrf(request))
    args['client'] = Clients.objects.get(id=clients_id)
    return render_to_response('client.html', args)

def index(request):
    t = get_template('index.html')
    html = t.render()
    return HttpResponse(html)

def addclient(request):
    client_form = ClientsForm
    args = {}
    args.update(csrf(request))
    args['form'] = client_form
    return render_to_response('clientform.html', args)


def postclient(request):
    if request.POST:
        client = Clients(request.POST)
        client.save()


    return redirect('/clients/all/')