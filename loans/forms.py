from django import forms
from django.forms import ModelForm
from .models import Loans
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loans
        fields = "__all__"

class LoanForm1(forms.ModelForm):
    class Meta:
        model = Loans
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'city', 'zip', 'date_out', 'date_in']
        
        