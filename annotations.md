# Iniciar o projeto Django e venv

```shell
pip freeze
python -m venv venv
. venv/bin/activate
source venv/Scripts/activate
pip install django
django-admin startproject project .
python manage.py startapp contact
```



# Configurar o git

```shell
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
```

# Migrando a base de dados do Django

```shell
python manage.py makemigrations
python manage.py migrate
```

# Criando e modificando a senha de um super usuário Django

```shell
python manage.py createsuperuser
python manage.py changepassword USERNAME
```

# Coletando os arquivos estáticos

```shell
python manage.py collectstatic
```

# Trabalhando com o model do Django

```python
# Importe o módulo
from contact.models import Contact
# Cria um contato (Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()
# Cria um contato (Não lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)
# Seleciona um contato com id 10
# Retorna o contato
contact = Contact.objects.get(pk=10)  # primary key
# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()
# Seleciona todos os contatos ordenando por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')
```

# Configurar a URL de arquivos estáticos e imagens no servidor (urls.py)

```python
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```