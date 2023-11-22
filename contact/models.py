from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:  # nome que será exibido na tabela do admin
        return f"{self.name}"
    

# cada classe nos models corresponde a uma tabela que será criada pelo django com os atributos definidos
# podemos criar um registro na base de dados ao criar uma instância dessa clase, e utilizando a função save() -> Contact.save()
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)  # o blank quer dizer que pode ser deixado em branco
    created_date = models.DateTimeField(default=timezone.now)  # executa a função now para colocar esse valor por padrão na criação
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True) # foreign key
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    
    def __str__(self) -> str:  # nome que será exibido na tabela do admin
        return f"{self.first_name} {self.last_name}"