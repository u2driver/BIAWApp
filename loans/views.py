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
 items = Equipment.objects.order_by('category').all().values()
 clients = Loans.objects.all().values()
 template = loader.get_template('home.html')
 context = {
   'items': items,
   'clients': clients,
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

def update_loan(request, id):
  loan = Loans.objects.get(id=id)
  if request.method == 'POST':
    form = LoanForm(request.POST, instance=loan)
    if form.is_valid():
      if form.cleaned_data['date_in'] is not None:
        x = Equipment.objects.get(id=form.cleaned_data['equip_id'])
        x.checkedout = False
        x.save()
      form.save()
      return HttpResponseRedirect(reverse('home'))
  else:
    form = LoanForm(instance=loan)   
  return render(request, 'loan_update.html', {'form': form})

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

def del_equip(request, id):
  items = Equipment.objects.get(id=id)
  items.delete()
  return HttpResponseRedirect(reverse('home'))

def del_client(request, id):
  clients = Loans.objects.get(id=id)
  clients.delete()
  return HttpResponseRedirect(reverse('home'))

def display_client(request, id):
 clients = Loans.objects.filter(equip_id = id).values()
 template = loader.get_template('display_client.html')
 context = {
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