from django import forms
from django.forms.models import inlineformset_factory
from django.forms.models import BaseInlineFormSet
from myapp.models import *

#
# class BaseThemeFormset(BaseInlineFormSet):
#     pass
#
#
# ThemeFormset = inlineformset_factory(Protocol,
#                                      Theme,
#                                      formset=BaseInlineFormSet,
#                                      extra=1)


# def add_fields(self, form, index):
#     super(BaseThemeFormset, self).add_fields(form, index)

from django import forms
from django.contrib.auth.models import User
from myapp.models import Employee
from django.core.validators import ValidationError


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        password2 = cleaned_data['password2']
        if password != password2:
            raise ValidationError("Паролли не совпадают")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class ProtocolForm(forms.ModelForm):
    class Meta:
        model = Protocol
        fields = '__all__'


ThemeFormset = inlineformset_factory(Protocol, Theme, extra=3, fields=('name',))
