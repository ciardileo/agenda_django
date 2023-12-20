from django import forms
from django.core.exceptions import ValidationError
from . import models


# classe que gera um form automática para o model, com todos os campos que quisermos
class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'category', 'description',)
        
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
        self.add_error(
            'first_name', ValidationError("Erro desconhecido", code=9)
        )
        
        return super().clean()
    
    # podemos fazer a validação de forma específica para cada campo
    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        print("Paseei aqui")
        
        if first_name.lower() == "davi":
            raise ValidationError("Nome não compatível")
        
        return first_name
    
