from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
# from myapp import
from django.forms.models import inlineformset_factory

from myapp import form
from myapp.form import ProtocolForm, UserForm, LoginForm, EmployeeForm, ThemeFormset
from django.views.generic import ListView
from myapp.models import *


# Create your views here.
class EmployeeView(ListView):
    template_name = "employee.html"
    queryset = Employee.objects.all()
    context_object_name = "employees"


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = UserForm()
    context = {
        "form": form
    }
    return render(request, "register.html", context)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("/")
        else:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, "login.html", context={
        "form": form
    })


def logout_view(request):
    logout(request)
    return redirect("/login/")


# def manage_theme(request, protocol_id):
#     protocol = get_object_or_404(models.Protocol, id=protocol_id)

#     if request.method == 'POST':
#         formset = form.ThemeFormset(request.POST, instance=protocol)
#         if formset.is_valid():
#             formset.save()
#             return redirect('parent_view', protocol_id=protocol.id)
#     else:
#         formset = form.ThemeFormset(instance=protocol)

#     return render(request, 'manage_theme.html', {
#         'protocol': protocol,
#         'theme_formset': formset})


@transaction.atomic
def create_protocol(request):
    protocol_form = ProtocolForm(request.POST or None)

    if request.method == "POST":
        if protocol_form.is_valid():
            protocol_instance = protocol_form.save(commit=False)
            protocol_instance.secretary = request.user
            protocol_instance.save()
            theme_form_set = ThemeFormset(request.POST or None, instance=protocol_instance)
            if theme_form_set.is_valid():
                theme_form_set.save()
            return redirect("/")
    theme_form_set = ThemeFormset(request.POST or None)
    context = {
        "protocol_form": protocol_form,
        "theme_form_set": theme_form_set,
    }
    return render(request, 'manage_theme.html', context)

# def pro_formset(request):
#     form = datasiswa(request.POST or None)
#     FormSet2 = inlineformset_factory(Protocol, Theme, extra=2)
#     if request.method == 'POST':
#         if form.is_valid():
#             protocol = form.save
