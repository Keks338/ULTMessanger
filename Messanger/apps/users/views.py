from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, CustomUserForm
from .models import CustomUser
# from ecommerce.apps.catalog.models import Product, Advert, Undcat, Category

def signUp(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация произошла успешно!")
            return redirect("users:loginPage")
        messages.error(request, "При регистрации произошла ошибка")
    else:
        form = NewUserForm()
    return render(request, "users/sign-up.html", {
        'form': form
    })


def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Добро пожаловать, {username}!")
                return redirect("messanges:homePage")
            else:
                messages.error(request, "При входе произошла ошибка.")
        else:
            messages.error(request, "При входе произошла ошибка.")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {
        'form': form
    })


def edit_user(request, user_id):
    user = CustomUser.objects.get(pk=user_id)

    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("messanges:homePage")
    else:
        form = CustomUserForm(instance=user)

    return render(request, 'users/user-edit.html', {'form': form})

def profilePage(request, user_id):
    profile = CustomUser.objects.get(pk=user_id)
    return render(request, "users/user-profile.html", {
        'profile': profile
    })


def logoutUser(request):
    logout(request)
    messages.info(request, "Вы вышли из аккаунта.")
    return redirect("messanges:homePage")

# def adminPage(request):
#     products = Product.objects.all()
#     adverts = Advert.objects.all()
#     subcats = Undcat.objects.all()
#     categories = Category.objects.all()
#     return render(request, "users/adminPage.html", {
#         'products': products,
#         'adverts': adverts,
#         'subcats': subcats,
#         'categories': categories,
#     })
