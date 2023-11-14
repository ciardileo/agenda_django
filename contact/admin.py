from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'description')  # campos que serão mostrados na tabela 
    ordering = ("-id",)  # ordena o id por ordem decrescente
    list_filter = ('created_date',)  # filtro
    search_fields = ('id', 'first_name', 'last_name',)  # campos que podem ser pesquisados
    list_per_page = 10  # registros por página
    list_max_show_all = 50  # máximo de páginas mostradas no "mostrar tudo"
    list_editable = ('email',)  # poder editar campo pela tabela mesmo
    list_display_links = ('id', 'first_name', 'last_name')  # elementos que terão um link para a página do registro