from django import forms
from django.core.exceptions import ValidationError
from . import models


# classe que gera um form automática para o model, com todos os campos que quisermos
class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'category', 'description',)
    
    # usamos esse método para adicionar erros específicos
    def clean(self):
        cleaned_data = self.cleaned_data
        
        print(cleaned_data)
        
        
        self.add_error(
			'first_name', ValidationError("Erro desconhecido", code=9)
		)
        
        return super().clean()
        
		
        
        
