from django.shortcuts import render
from .forms import LoginForm, RegistrationForm, EditForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
'''def login(request):
    title = "Вход для клиентов"
    form = LoginForm
    context = {
        "title": title,
        "form": form,
        "next": "/products",
    }
    if request.method == 'POST' and form.is_valid():


    return render(request, "login.html", context)
'''


def register(request):
    title = "Регистрация пользователя"

    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("login"))
    else:
        form = RegistrationForm()

    context = {
        "title": title,
        "form": form,
        "next": "/",
    }
    return render(request, 'registration/register.html', context)


@login_required
def edit(request):
    title = "Редактирование пользователя"

    if request.method == "POST":
        form = EditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()

    else:
        form = EditForm(instance=request.user)

    context = {
        "title": title,
        "form": form,
        "next": "/",
    }
    return render(request, 'registration/edit.html', context)
