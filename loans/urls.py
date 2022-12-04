from django.urls import path
from loans import views

urlpatterns = [
   path("", views.home, name="home"),
   path('add/', views.add, name='add'),
   path('add/addrecord/', views.addrecord, name='addrecord'),
   path('update/<int:id>', views.update, name='update'),
   path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
   path('add_loan/', views.add_loan, name='add_loan'),
   path('update_loan/<int:id>', views.update_loan, name='update_loan'),
   path('add1/', views.add1, name='add1'),
   path('add1/addrecord1/', views.addrecord1, name='addrecord1'),
   path('update1/<int:id>', views.update1, name='update1'),
   path('update1/updaterecord1/<int:id>', views.updaterecord1, name='updaterecord1'),
   
   path('del_equip/<int:id>', views.del_equip, name='del_equip'),
   path('del_client/<int:id>', views.del_client, name='del_client'),
   
   path('testing/', views.testing, name="testing"),
]
