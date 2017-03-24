from django import forms

from .models import Clients, EventInfo, Hall

class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients
        exclude = []


class EventInfoForm(forms.ModelForm):
    event_info_name = forms.CharField(label=u'Название')
    event_info_description = forms.CharField(label=u'Описание',max_length=1000, widget=forms.TextInput({}))
    event_info_poster = forms.ImageField(label=u'Афиша', required=False)
    class Meta:
        model = EventInfo
        fields = ('event_info_name', 'event_info_description', 'event_info_poster')


class HallForm(forms.ModelForm):
    hall_name = forms.CharField(label=u'Название зала')
    hall_address = forms.CharField(label = u'Адресс зала')
    class Meta:
        model = Hall
        fields = ('hall_name', 'hall_address')