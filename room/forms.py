from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignupUserForm(UserCreationForm):
    email = forms.EmailField(help_text='Required. Type a valid email address.')
    first_name = forms.CharField(max_length=50, required=True, help_text='Required. 50 characters or fewer.')
    last_name = forms.CharField(max_length=50, required=True, help_text='Required. 50 characters or fewer.')
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2']