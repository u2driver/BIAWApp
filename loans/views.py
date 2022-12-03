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
 
def home(request):
 items = Equipment.objects.all().values()
 clients = Loans.objects.all().values()
 template = loader.get_template('home.html')
 context = {
   'items': items,
   'clients': clients,
 }
 return HttpResponse(template.render(context, request))
 
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
