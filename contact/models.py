from django.db import models
from django.utils import timezone

# Create your models here.

# cada classe nos models corresponde a uma tabela que será criada pelo django com os atributos definidos
# podemos criar um registro na base de dados ao criar uma instância dessa clase, e utilizando a função save() -> Contact.save()
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)  # o blank quer dizer que pode ser deixado em branco
    created_date = models.DateTimeField(default=timezone.now)  # executa a função now para colocar esse valor por padrão na criação
    description = models.TextField(blank=True)
    
    def __str__(self) -> str:  # nome que será exibido na tabela do admin
        return f"{self.first_name} {self.last_name}"