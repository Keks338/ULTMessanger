from django.shortcuts import render
from .models import CustomUser

def homePage(request):
    hide_element = False
    Users = CustomUser.objects.all()
    return render(request, "messanger/index.html", {
        'hide_element': hide_element,
        'Users': Users
    })
