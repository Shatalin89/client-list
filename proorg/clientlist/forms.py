from django.forms import ModelForm, ImageField

from .models import Clients, EventInfo

class ClientsForm(ModelForm):
    class Meta:
        model = Clients
        exclude = []


class EventInfoForm(ModelForm):
    event_info_poster = ImageField(label=u'Аватар', required=False)
    class Meta:
        model = EventInfo
        fields = ('event_info_name', 'event_info_description', 'event_info_poster')