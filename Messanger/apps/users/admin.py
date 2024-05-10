from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'short_Desc', 'birthdate', 'image', 'is_Blocked', 'blocked_Time')
    list_filter = ('is_active', 'is_staff', 'is_Blocked',)  # Добавляем is_Blocked в list_filter
    search_fields = ('username', 'email', 'first_name', 'last_name',)  # Избегаем проблемы с 'short_Desc', 'birthdate', 'image', 'is_Blocked', 'blocked_Time'

CustomUser = get_user_model()
admin.site.register(CustomUser, CustomUserAdmin)
