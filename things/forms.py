from django import forms
from .models  import Thing

class ThingForm():
    name = forms.CharField(label='name')
    description = forms.charField(
        label = 'description'
        widget={forms.Textarea()}
    )
    quantity = forms.NumberInput(
        label = 'quantity'
    )