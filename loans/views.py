import re
from django.utils.timezone import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template import loader
from .models import Equipment
 
def home(request):
 items = Equipment.objects.all().values()
 template = loader.get_template('home.html')
 context = {
   'items': items,
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

def testing(request):
 items = Equipment.objects.filter(category = 'wheelchair', condition = 'good').values()
 template = loader.get_template('template.html')
 context = {
   'items': items,
 }
 return HttpResponse(template.render(context, request))
