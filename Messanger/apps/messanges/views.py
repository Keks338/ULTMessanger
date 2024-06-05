from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from ..messanges.models import Chat, GroupChat, MessageText
import json
import random

def homePage(request):
    user = request.user
    hide_element = False
    Users = CustomUser.objects.all().order_by("username")
    massa = []
    if user.is_authenticated:
        Chats = Chat.objects.filter(User1=user) | Chat.objects.filter(User2=user)
        for i in Chats:
            massa.append(i.User1.id)
            massa.append(i.User2.id)
            if i.User1.id == i.User2.id:
                massa.append(i.User1)
    else:
        Chats = Chat.objects.all()
    GroupChats = GroupChat.objects.all()
    chat_exists = Chats.exists()

    return render(request, "messanger/index.html", {
        'chat_exists': chat_exists,
        'hide_element': hide_element,
        'Users': Users,
        'Chats': Chats,
        'GroupChats': GroupChats,
        'massa': massa,
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

def add_chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data_user_id = data["userId"]
        try:
            user_id = CustomUser.objects.get(id=data_user_id)
            user = CustomUser.objects.get(id=request.user.id)
            chat_db = Chat(User1=user_id, User2=user)
            chat_db.save()
            return JsonResponse({'status': 'success', 'userId': data})  # Возвращаем ID добавленного друга
        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Пользователь не найден'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})  # Обработка других исключений
    else:
        return JsonResponse({'status': 'error', 'message': 'Метод не поддерживается'})

def remove_chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data_user_id = data["userId"]
        try:
            user_id = CustomUser.objects.get(id=data_user_id)
            user = CustomUser.objects.get(id=request.user.id)
            print(user, user_id)
            Chat.objects.filter(User1=user_id, User2=user).delete()
            Chat.objects.filter(User1=user, User2=user_id).delete()
            return JsonResponse({'status': 'success', 'userId': data})  # Возвращаем ID добавленного друга
        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Пользователь не найден'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})  # Обработка других исключений
    else:
        return JsonResponse({'status': 'error', 'message': 'Метод не поддерживается'})

def get_messages(request, chat_id):
    if request.method == 'GET':
        messages = MessageText.objects.filter(Chat_id=chat_id).order_by('Message_Creation_Date')
        messages_list = [{'sender': message.Sender.username, 'text': message.Text, 'date': message.Message_Creation_Date.strftime('%Y-%m-%d %H:%M:%S')} for message in messages]
        return JsonResponse(messages_list, safe=False)

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        chat_id = data['chat_id']
        text = data['text']
        user = request.user
        try:
            chat = Chat.objects.get(id=chat_id)
            message = MessageText(Chat_id=chat, Text=text, Sender=user)
            message.save()
            return JsonResponse({'status': 'success'})
        except Chat.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Чат не найден'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Метод не поддерживается'})