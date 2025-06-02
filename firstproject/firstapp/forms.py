from django import forms
from . models import reservation

class ReservationForms(forms.ModelForm):
    class Meta:
        model = reservation
        fields = ['fname', 'lname', 'guests', 'comments', ]  
