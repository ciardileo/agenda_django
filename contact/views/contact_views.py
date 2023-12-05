from django.shortcuts import render
from contact.models import Contact
from django.http import Http404

# Create your views here.

def index(request):
	contact = Contact.objects.filter(show=True)
	
	context = {
		'contacts': contact
	}
	
	return render(request, "contact/index.html", context)


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