from django import forms
from .models import UserBase
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from django_countries.widgets import CountrySelectWidget


class UserLoginForm(AuthenticationForm):

    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control mb-3', 'placeholder':'Username','id':'login-username'
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control mb-3',
        'placeholder':'Password',
        'id':'login-pwd'
    }))


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(label='Account email(can not be changed)',max_length=200,widget=forms.EmailInput(
        attrs={'class':'form-control mb-3','placeholder':'email','id':'form-email','readonly':'readonly'}
    ))
    user_name = forms.CharField(label='Username',min_length=4,max_length=50,widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username','id': 'form-username', 'readonly': 'readonly'}
    ))
    name = forms.CharField(label='Name', min_length=4, max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Name','id': 'form-name'}
    ))
    
    class Meta:
        model = UserBase
        fields = ('email','user_name','name')


class RegistrationForm(forms.ModelForm):

    user_name = forms.CharField(label='Username',min_length=4,max_length=10,help_text='Required',widget=forms.TextInput())

    email = forms.EmailField(label='Email', max_length=100, help_text='Required',widget=forms.EmailInput())

    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput())

    class Meta:
        model = UserBase
        fields = ('user_name','email')

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError('Username already exists!')
        return user_name
    
    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password2'] != cd['password']:
            raise forms.ValidationError('Passwords do not match!')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError('An user with that email already exists, please use another one.')
        return email

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['user_name'].widget.attrs.update({
            'class':'form-control mb-3','placeholder':'Enter Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Enter Email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Enter Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Repeat Password'})


class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254,widget=forms.EmailInput(
        attrs={'class':'form-control mb-3','placeholder':'Email','id':'form-email'}
    ))

    def clean_email(self):
        email=self.cleaned_data['email']
        u=UserBase.objects.filter(email=email)
        if not u:
            raise forms.ValidationError('Unfortunately we can not find that email address.')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class':'form-control mb-3','placeholder':'New Password','id':'form-newpass1'}
    ))

    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3',
                   'placeholder': 'New Password', 'id': 'form-newpass2'}
        ))
