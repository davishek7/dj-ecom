from django import forms
from .models import UserBase


class RegistrationForm(forms.ModelForm):

    user_name = forms.CharField(label='Enter Username',min_length=4,max_length=10,help_text='Required',widget=forms.TextInput(attrs={'class':'form-control mb-4'}))
    email = forms.EmailField(label='Enter Email', max_length=100, help_text='Required', error_messages={
                             'required': 'Sorry, you will need an email'}, widget=forms.EmailInput(attrs={'class': 'form-control mb-4'}))
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-4'}))

    class Meta:
        model = UserBase
        fields = ('user_name','email')
