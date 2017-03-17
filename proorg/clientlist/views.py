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

def client(request, clients_id):
    args ={}
    args.update(csrf(request))
    args['client'] = Clients.objects.get(id=clients_id)
    args['status'] = 'disabled'
    return render_to_response('client.html', args)

def index(request):
    t = get_template('index.html')
    html = t.render()
    return HttpResponse(html)

def addclient(request):
    args ={}
    args.update(csrf(request))
    args['status'] = 'enable'
    return render_to_response('client.html', args)


def postclient(request):
    if request.POST:
        clients_name = request.POST['clients_name']
        clients_middlename = request.POST['clients_middlename']
        clients_lastname = request.POST['clients_lastname']
        clients_age = request.POST['clients_age']
        clients_telephone = request.POST['clients_telephone']
        clients_email = request.POST['clients_email']
        clients_comments = request.POST['clients_comments']
        client = Clients(clients_name = clients_name, clients_middlename = clients_middlename,clients_lastname = clients_lastname,clients_age = clients_age, clients_telephone= clients_telephone, clients_email = clients_email, clients_comments = clients_comments)
        client.save()
    return redirect('/clients/all/')


