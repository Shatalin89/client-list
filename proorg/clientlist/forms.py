from django.forms import ModelForm
from clientlist.models import Clients

class ClientsForm(ModelForm):
    class Meta:
        model = Clients
        exclude = []