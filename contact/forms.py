from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from . import models


# classe que gera um form automática para o model, com todos os campos que quisermos
class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': "image/*"
            }
        )
    )
    
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'category', 'description', 'picture')
        
        # podemos configurar os campos html
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': "Escreva apenas o primeiro nome"
                }
            ),
        }
    
    # usamos esse método para adicionar erros específicos
    def clean(self):
        cleaned_data = self.cleaned_data
        
        print(cleaned_data)
        
        # podemos adicionar erros específicos
        if cleaned_data['first_name'] == cleaned_data['last_name']:
            self.add_error('last_name', ValidationError('O primeiro nome não pode ser igual ao último', code=10))
        
        return super().clean()
    
    # podemos fazer a validação de forma específica para cada campo
    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")

        
        if first_name.lower() == "davi":
            raise ValidationError("Nome não compatível")
        
        return first_name

# classe que gera um form de criação de usuários 
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email', ValidationError("Esse email já foi utilizado")
            )