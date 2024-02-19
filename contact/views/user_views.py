from django.shortcuts import render
from contact.forms import RegisterForm
from django.contrib import messages

def register(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuário criado com sucesso!")
        else:
            messages.error(request, "Erro desconhecido, tente novamente")
    
    
    context = {
        'form': RegisterForm()
    }
    
    return render(
      request, 'contact/register.html', context
    )