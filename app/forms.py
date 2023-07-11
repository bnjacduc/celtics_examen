from django import forms 
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo', 'nombre', 'precio', 'img')



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    # Agrega otros campos adicionales aquí

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'password1', 'password2')
