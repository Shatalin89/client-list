from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from .models import Clients, EventInfo, Event
from .models import Hall, PlaceInfo, PlaceScheme, PlaceSector
from django.template.loader import get_template
from .forms import ClientsForm, EventInfoForm, HallForm, PlaceInfoForm
from django.template.context_processors import csrf
from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import get_object_or_404


# Create your views here.


#Список всех клиентов
def clients(request):
    return render_to_response('clientlist.html', {'clients': Clients.objects.all()})


#Удаление клиента
def client_del(request, clients_id):
    client = Clients.objects.get(id=clients_id)
    client.delete()
    return redirect('/clients/all/')


#Главная страница
def index(request):
    t = get_template('index.html')
    html = t.render()
    return HttpResponse(html)


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


#Просмотр одного клиента
def client(request, clients_id):
    args ={}
    args.update(csrf(request))
    args['client'] = Clients.objects.get(id=clients_id)
    args['status'] = 'disabled'
    args['action'] = 'view'
    return render_to_response('client.html', args)


#Вызов страницы добавления клиента
def addclient(request):
    args ={}
    args.update(csrf(request))
    args['status'] = 'enable'
    args['action'] = 'add'
    return render_to_response('client.html', args)


#Вызов страницы редактирования клиента
def show_client_edit(request, clients_id):
    args ={}
    args.update(csrf(request))
    args['client'] = Clients.objects.get(id=clients_id)
    args['status'] = 'enable'
    args['action'] = 'edit'
    return render_to_response('client.html', args)


#Применение изменения редактирования клиента
def client_edit(request, clients_id):
    client = Clients.objects.get(id=clients_id)
    if request.POST:
        client.clients_name = request.POST['clients_name']
        client.clients_middlename = request.POST['clients_middlename']
        client.clients_lastname = request.POST['clients_lastname']
        client.clients_age = request.POST['clients_age']
        client.clients_telephone = request.POST['clients_telephone']
        client.clients_email = request.POST['clients_email']
        client.clients_comments = request.POST['clients_comments']
        client.save()
        return redirect('/clients/all/')


#Новая запись информации о мероприятии
def event_info_new(request):
    if request.method == 'POST':
        form = EventInfoForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.data_add = timezone.now()
            post.save()
            return redirect('/eventsinfo/all/')
    else:
        form = EventInfoForm()
        return render(request, 'event.html', {'form': form})


def event_info_edit(request, events_info_id):
    event_info = get_object_or_404(EventInfo, id=events_info_id)
    print(events_info_id)
    if request.method == "POST":
        form = EventInfoForm(request.POST, request.FILES, instance=event_info)
        if form.is_valid():
            event_info = form.save(commit=False)
            event_info.data_add = timezone.now()
            event_info.save()
            return redirect('/eventsinfo/all/')
    else:
        form = EventInfoForm(instance=event_info)
    return render(request, 'event.html', {'form': form})


#Список всех мероприятий
def get_event_info(request):
    return render_to_response('eventinfo.html', {'eventinfo': EventInfo.objects.all()})


#удаление мероприятия
def delevents(request, events_info_id):
    events_info = EventInfo.objects.get(id=events_info_id)
    events_info.delete()
    return redirect('/eventsinfo/all/')


def get_hall_info(request):
    return render_to_response('halls.html', {'hallinfo': Hall.objects.all()})


def add_hall_info(request):
    if request.POST:
        form = HallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hallinfo/all/')
    else:
        form = HallForm()
        return render(request, 'hall.html', {'form': form})


def del_hall_info(request, hall_info_id):
    hall_info = Hall.objects.get(id=hall_info_id)
    hall_info.delete()
    return redirect('/hallinfo/all/')


def edit_hall_info(request, hall_info_id):
    hall_info = get_object_or_404(Hall, id=hall_info_id)
    if request.method == "POST":
        form = HallForm(request.POST, instance=hall_info)
        if form.is_valid():
            hall_info = form.save(commit=False)
            hall_info.save()
            return redirect('/hallinfo/all/')
    else:
        form = HallForm(instance=hall_info)
    return render(request, 'hall.html', {'form': form})


def get_place_info(request):
    args = {}
    args.update(csrf(request))
    args['places'] = PlaceInfo.objects.all()
    return render_to_response('places.html', args)


def add_place_info(request):
    if request.POST:
        form = PlaceInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/placeinfo/all/')
    else:
        form = PlaceInfoForm()
        return render(request, 'placescheme.html', {'form': form})


def add_place_scheme(request, place_info_id):
    if request.POST:
        count = int(request.POST['place_count'])
        place_info = PlaceInfo.objects.get(id=place_info_id)
        max_count = place_info.place_sheme_hall.hall_max_places
        if place_info.place_type_scheme.id == 1:
            place_sector = PlaceSector.objects.get(id=1)
            if count < max_count:
                for i in range(count):
                    place_sceheme = PlaceScheme(place_name='Входной №' + str(i+1), place_raw=1, place_places=i+1, place_sector=place_sector, place_scheme_id=place_info, place_x=30 * i, place_y=0)
                    place_sceheme.save()
                place_info.place_flag_set_sceme = True
                place_info.save()
        return redirect('/placeinfo/all/')


def add_event(request):
    epp = PlaceScheme.objects.get(place_scheme_id=1)