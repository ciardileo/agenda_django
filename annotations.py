"""
arquivo de anotações dos comandos
"""

# sql indireto usando os models:

c = Contact(first_name="Regis")
c.save()

c.last_name = "Tadeu"
c.email = "sla@gmail.com"
c.phone = "11945968686"
c.save() # salva as alterações

Contact.objects.all()  # select all

