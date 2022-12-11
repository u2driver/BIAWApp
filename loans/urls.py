from django.urls import path
from loans import views

urlpatterns = [
   path("", views.home, name="home"),
   path('display_loan/<int:id>', views.display_loan, name = 'display_loan'),
   path('add/', views.add, name='add'),
   path('add/addrecord/', views.addrecord, name='addrecord'),
   path('update/<int:id>', views.update, name='update'),
   path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
   path('add_loan/', views.add_loan, name='add_loan'),
   path('update_loan/<int:id>', views.update_loan, name='update_loan'),
   path('del_equip/<int:id>', views.del_equip, name='del_equip'),
   path('del_client/<int:id>', views.del_client, name='del_client'),
   
   path('display_client/<int:id>', views.display_client, name="display_client"),
]
