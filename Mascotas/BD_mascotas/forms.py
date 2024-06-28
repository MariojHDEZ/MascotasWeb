from django import forms
from .models import Post, Contacto

class BlogForms(forms.ModelForm):
    
    class Meta:
        model=Post
        
        fields='__all__'
    #field=['imagen]

class ContactoForms(forms.ModelForm):
    
    class Meta:
        model=Contacto
        
        fields='__all__'