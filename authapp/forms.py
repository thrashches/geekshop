from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'age', 'password1', 'password2', 'photo', 'email']


class EditForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'age', 'password1', 'password2', 'photo', 'email']
