from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
import json
import random

def homePage(request):
    hide_element = False
    Users = CustomUser.objects.all().order_by("username")
    return render(request, "messanger/index.html", {
        'hide_element': hide_element,
        'Users': Users,
    })

def remove_friend(request):
    if request.method == 'POST':
        data2 = json.loads(request.body)
        data = data2["userId"]
        try:
            user = CustomUser.objects.get(id=request.user.id)
            if user.friend_list_id and int(data) in user.friend_list_id:
                user.friend_list_id.remove(int(data))  # Удаляем пользователя из списка друзей
                user.save()
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Пользователь не найден в списке друзей'})
        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Пользователь не найден'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Метод не поддерживается'})


def remove_friend_p(request):
    if request.method == 'POST':
        data2 = json.loads(request.body)
        data = data2["userId"]
        data = int(data)
        try:
            user = CustomUser.objects.get(id=request.user.id)
            for i in CustomUser.objects.all():
                if data == i.id:
                    data = i
            if data.friend_list_id and int(user.id) in data.friend_list_id:
                data.friend_list_id.remove(int(user.id))  # Удаляем пользователя из списка друзей
                data.save()
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Пользователь не найден в списке друзей'})
        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Пользователь не найден'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Метод не поддерживается'})

def add_friend(request):
    if request.method == 'POST':
        data2 = json.loads(request.body)
        data = data2["userId"]
        print(data)
        try:
            user = CustomUser.objects.get(id=request.user.id)
            user.friend_list_id.append(int(data))  # Добавляем друга в список
            user.save()
            return JsonResponse({'status': 'success', 'userId': data})  # Возвращаем ID добавленного друга
        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Пользователь не найден'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})  # Обработка других исключений
    else:
        return JsonResponse({'status': 'error', 'message': 'Метод не поддерживается'})

