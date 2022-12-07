import re
from django.utils.timezone import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template import loader
import loans.models
from loans import models
from .models import Equipment
from .models import Loans
from .forms import LoanForm
 
def home(request):
 items = Equipment.objects.all().values()
 clients = Loans.objects.all().values()
 template = loader.get_template('home.html')
 context = {
   'items': items,
   'clients': clients,
 }
 return HttpResponse(template.render(context, request))

def display_loan(request, id):
  items = Equipment.objects.get(id=id)
  template = loader.get_template('display_loan.html')
  context = {
    'items': items,
}
  return HttpResponse(template.render(context, request)) 
  

def add_loan(request):
  # create object of form
  if request.method == 'POST':
    loan = LoanForm(request.POST)
  # check if form data is valid
    if loan.is_valid():
      #check to see if equipment is already checked out:
      x = Equipment.objects.get(id=loan.cleaned_data['equip_id'])
      if x.checkedout:
        return HttpResponse("That equipment is already checked out")
      # if equipment is available, save the form data to model
      else:
        loan.save()
        x.checkedout = True
        x.save()
      return HttpResponseRedirect(reverse('home'))
  else:
    loan = LoanForm
  return render(request, "loan.html", {'form': loan})

 
def add(request):
 template = loader.get_template('add.html')
 return HttpResponse(template.render({}, request))


def addrecord(request):
 v = request.POST['invnumber']
 w = request.POST['category']
 x = request.POST['description']
 y = request.POST['condition']
 z = request.POST['checkedout']
 items = Equipment(invnumber = v, category = w, description = x, condition = y, checkedout = z)
 items.save()
 return HttpResponseRedirect(reverse('home'))

def update(request, id):
 items = Equipment.objects.get(id=id)
 template = loader.get_template('update.html')
 context = {
   'items': items,
 }
 return HttpResponse(template.render(context, request))
 
def updaterecord(request, id):
 invnumber = request.POST['invnumber']
 category = request.POST['category']
 description = request.POST['description']
 condition = request.POST['condition']
 checkedout = request.POST['checkedout']
 items = Equipment.objects.get(id=id)
 items.invnumber = invnumber
 items.category = category
 items.description = description
 items.condition = condition
 items.checkedout = checkedout
 
 items.save()
 return HttpResponseRedirect(reverse('home'))

def add1(request):
 template = loader.get_template('add1.html')
 return HttpResponse(template.render({}, request))

def addrecord1(request):
 p = request.POST['first_name']
 q = request.POST['last_name']
 r = request.POST['phone_number']
 s = request.POST['address']
 t = request.POST['city']
 u = request.POST['zip']
 v = request.POST['date_out']
 w = request.POST['date_in']
 x = request.POST['equip_id']
 clients = Loans(first_name = p, last_name = q, phone_number = r, address = s, city = t, zip = u, date_out = v, date_in= w, equip_id=x)
 clients.save()
 return HttpResponseRedirect(reverse('home'))

def update1(request, id):
 clients = Loans.objects.get(id=id)
 template = loader.get_template('update1.html')
 context = {
   'clients': clients,
 }
 return HttpResponse(template.render(context, request))
 
def updaterecord1(request, id):
 first_name = request.POST['first_name']
 last_name = request.POST['last_name']
 phone_number = request.POST['phone_number']
 address = request.POST['address']
 city = request.POST['city']
 zip = request.POST['zip']
 date_out = request.POST['date_out']
 date_in = request.POST['date_in']
 equip_id = request.POST['equip_id']
 clients = Loans.objects.get(id=id)
 clients.first_name = first_name
 clients.last_name = last_name
 clients.phone_number = phone_number
 clients.address = address
 clients.city = city
 clients.zip = zip
 clients.date_out = date_out
 clients.date_in = date_in
 clients.equip_id = equip_id
 clients.save()
 return HttpResponseRedirect(reverse('home'))

def update_loan(request, id):
  loan = Loans.objects.get(id=id)
  
  if request.method == 'POST':
    form = LoanForm(request.POST, instance=loan)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('home'))
  else:
    form = LoanForm(instance=loan)
      
  return render(request, 'loan_update.html', {'form': form})

def del_equip(request, id):
  items = Equipment.objects.get(id=id)
  items.delete()
  return HttpResponseRedirect(reverse('home'))

def del_client(request, id):
  clients = Loans.objects.get(id=id)
  clients.delete()
  return HttpResponseRedirect(reverse('home'))

def testing(request):
 items = Equipment.objects.filter(category = 'Wheel Chair', condition = 'Good').values()
 template = loader.get_template('template.html')
 context = {
   'items': items,
 }
 return HttpResponse(template.render(context, request))
