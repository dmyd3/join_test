from django import forms
from django.forms import ModelForm
from q7.models import Alvo

# class AlvoForm(ModelForm):
#     class Meta:
#         model = Alvo
#         fields = ['nome', 'latitude', 'longitude', 'expiration_date']

class AlvoForm(forms.Form):

    nome = forms.CharField(
        required=True, max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    latitude = forms.FloatField(
        required=True, min_value=-90.0, max_value=90.0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    
    longitude = forms.FloatField(
        required=True, min_value=-180.0, max_value=180.0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    expiration_date = forms.DateTimeField(
        required=True,
        widget=forms.DateInput(attrs={'class': 'datepicker form-control', 'placeholder':'Clique para selecionar'})
    )
    