from django import forms
from django.forms import fields
from .models import Todo


class TodoAddForm (forms.ModelForm):
    class Meta:
        model= Todo
        fields=('title',)
        # , tupple olduğu için konuldu yoksa hata verir
        # exclude=('title',)  title hariç hepsi
        
class TodoUpdateForm (forms.ModelForm):
    class Meta:
        model=Todo
        fields=('title', 'completed')
        
        
        

        