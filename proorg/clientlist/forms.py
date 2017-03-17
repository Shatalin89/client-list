from django.forms import ModelForm
from .models import Clients, EventInfo

class ClientsForm(ModelForm):
    class Meta:
        model = Clients
        exclude = []


class EentInfoForm(ModelForm):
    class Meta:
        model = EventInfo
        exclude = []