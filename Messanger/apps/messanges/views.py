from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
import json

def homePage(request):
    hide_element = False
    Users = CustomUser.objects.all()
    return render(request, "messanger/index.html", {
        'hide_element': hide_element,
        'Users': Users,
    })

@csrf_exempt
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

def add_friend(request):
    if request.method == 'POST':
        data2 = json.loads(request.body)
        data = data2["userId"]
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

