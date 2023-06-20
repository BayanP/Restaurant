from django.forms import ModelForm, TextInput, EmailInput, DateInput, TimeInput, Textarea
from .models import Reservation, Contact

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['full_name', 'email','phone','date','time','persons','message']
        widgets = {
            'full_name': TextInput(attrs={
                'name':'name',
                'class':'form-control',
                'id':'name',
                'placeholder':'your name',
                'data-rule':'minlen:4',
                'data-msg':'enter'
            }),
            'email': EmailInput(attrs={
                'name':'email',
                'class':'form-control',
                'id':'email',
                'placeholder':'your email',
                'data-rule':'minlen:4',
                'data-msg':'enter'
            }),
            'phone': TextInput(attrs={
                'name':'phone',
                'class':'form-control',
                'id':'phone',
                'placeholder':'your phone',
                'data-rule':'minlen:4',
                'data-msg':'enter'
            }),
            'date': DateInput(attrs={
                'name':'date',
                'class':'form-control',
                'id':'date',
                'placeholder':'date',
                'data-rule':'minlen:4',
                'data-msg':'enter'
            }),
            'time': TimeInput(attrs={
                'name':'time',
                'class':'form-control',
                'id':'time',
                'placeholder':'time',
                'data-rule':'minlen:4',
                'data-msg':'enter'
            }),
            'persons': TextInput(attrs={
                'name':'persons',
                'class':'form-control',
                'id':'persons',
                'placeholder':'persons',
                'data-rule':'minlen:4',
                'data-msg':'enter'
            }),
            'message': Textarea(attrs={
                'name':'message',
                'class':'form-control',
                'id':'message',
                'placeholder':'message',
                'data-rule':'minlen:4',
                'data-msg':'enter'
            }),
        }
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email','subject','message']
        widgets = {
            'full_name': TextInput(attrs={
                'name':'name',
                'class':'form-control',
                'id':'name',
                'placeholder':'your name',
                'data-rule':'minlen:4',
                'data-msg':'enter'
            }),
            'email': EmailInput(attrs={
                'name':'email',
                'class':'form-control',
                'id':'email',
                'placeholder':'your email',
                'data-rule':'minlen:4',
                'data-msg':'enter'
            }),
            'subject': TextInput(attrs={
                'name':'subject',
                'class':'form-control',
                'id':'subject',
                'placeholder':'persons',
                'data-rule':'minlen:4',
                'data-msg':'enter'
            }),
            'message': Textarea(attrs={
                'name':'message',
                'class':'form-control',
                'id':'message',
                'placeholder':'message',
                'data-rule':'minlen:4',
                'data-msg':'enter'
            }),
        }