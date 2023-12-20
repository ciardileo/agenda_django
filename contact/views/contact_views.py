from django.shortcuts import render
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from contact.forms import *



# Create your views here.

# página inicial
def index(request):
	contact = Contact.objects.filter(show=True)
 
	paginator = Paginator(contact, 10)
	page_number = request.GET.get("page")
	page_obj = paginator.get_page(page_number)
	
	context = {
		'contacts': page_obj
	}
	
	return render(request, "contact/index.html", context)


# página de pesquisa
def search(request):
	value = request.GET.get('q', '').strip()
 
	if value == '':
		return redirect('index')
	
	# icontains faz com que o filtro retorne caso o campo conter o que nós queremos pesquisar, e o I indica que não é case sensitive
	# essa função Q nos permite fazer o filtro como se fosse um "ou"
	contact = Contact.objects.filter(show=True).filter(Q(first_name__icontains=value) | Q(last_name__icontains=value) | Q(phone__icontains=value) | Q(email__icontains=value))
	
	paginator = Paginator(contact, 25)
	page_number = request.GET.get("page")
	page_obj = paginator.get_page(page_number)
	
	context = {
		'contacts': page_obj
	}

	return render(request, "contact/index.html", context)


# página de contato
def contact_page(request, id):
	print(f"contato {id}")
	
	try:
		contact = Contact.objects.get(pk=id)
  
		if contact.show == False:
			raise Http404("Esta página está restrita")
	
		context = {
			'id': contact.id,
			'first_name': contact.first_name,
			'last_name': contact.last_name,
			'phone': contact.phone, 
			'email': contact.email,
			'created_date': contact.created_date,
			'description': contact.description,
			'category': contact.category
		}
	except:
		raise Http404("Este contato não existe!")

 
	return render(  # renderiza um arquivo html para a view
		request, "contact/contact_page.html", context
	)
 

# página de criação de contato
def create_contact(request):
	if request.method == "POST":
		print("Você enviou um formulário")
		# print(request.POST.get("first_name"))
  
		context = {
			'form': ContactForm(request.POST)
		}
	else:
		print("Você está acessando a página")
		context = {
				'form': ContactForm()
			}
			
   
	return render(request, 'contact/create.html', context)