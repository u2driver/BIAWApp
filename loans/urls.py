from django.urls import path
from loans import views

urlpatterns = [
   path("", views.home, name="home"),
   path('add/', views.add, name='add'),
   path('add/addrecord/', views.addrecord, name='addrecord'),
   path('update/<int:id>', views.update, name='update'),
   path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
   path('testing/', views.testing, name="testing"),
]
