from django import forms


class LogInForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput())


# because PasswordInput is an attribute within forms
