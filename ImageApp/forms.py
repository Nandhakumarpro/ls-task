from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from  . models import  Images
from django.forms import ClearableFileInput


class registerForm ( forms.Form ) :
    username = forms.CharField ( required=True , max_length=100  , widget=forms.TextInput(attrs={'placeholder': 'username'}) )
    password = forms.CharField(  required=True , max_length=100 , widget=forms.PasswordInput(attrs={'placeholder': 'password'}) )


class imageAddForm( forms.Form ) :
    images = forms.ImageField ( required=True   ,widget= ClearableFileInput(attrs={'multiple': True})  , label="Add Your Images Here   ")
    # date = forms.DateField ( required=True , widget=AdminDateWidget  )

    class Meta :
        fields = ( "images"  )
    #
    # def save (self ) :
    #     print ( self.cleaned_data  )




