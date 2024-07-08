from django import forms
from django.contrib.auth.forms import UserCreationForm
from comparing.models import CustomUser

class ProductComparisonForm(forms.Form):
    product1 = forms.URLField(label="Product 1 URL")
    product2 = forms.URLField(label="Product 2 URL")

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')