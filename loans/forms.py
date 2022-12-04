from django import forms
from django.forms import ModelForm
from .models import Loans
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loans
        fields = "__all__"
        