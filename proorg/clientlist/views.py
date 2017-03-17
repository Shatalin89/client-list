from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from .models import Clients, EventInfo, Event
from django.template.loader import get_template
from clientlist.forms import ClientsForm
from django.template.context_processors import csrf
from django.shortcuts import redirect


# Create your views here.
#Список всех клиентов
def clients(request):
    return render_to_response('clientlist.html', {'clients': Clients.objects.all()})
#Список всех мероприятий
def get_event_info(request):
    return render_to_response('eventinfo.html', {'eventinfo': EventInfo.objects.all()})
#Просмотр одного клиента
def client(request, clients_id):
    args ={}
    args.update(csrf(request))
    args['client'] = Clients.objects.get(id=clients_id)
    args['status'] = 'disabled'
    return render_to_response('client.html', args)

#Главная страница
def index(request):
    t = get_template('index.html')
    html = t.render()
    return HttpResponse(html)

#Вызов страницы добавления клиента
def addclient(request):
    args ={}
    args.update(csrf(request))
    args['status'] = 'enable'
    return render_to_response('client.html', args)

#Обработка добавления клиента
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

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
