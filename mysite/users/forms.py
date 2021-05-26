from django import forms

class SignUpForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    username = forms.CharField('Username', max_length=100)
    email = forms.EmailField('Email', max_length=100)
    password = forms.CharField('Password', max_length=100, widget=forms.PasswordInput)
    confirm_pass = forms.CharField('Confirm Password', max_length=100, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField('Username', max_length=100)
    password = forms.CharField('Password', max_length=100, widget=forms.PasswordInput)