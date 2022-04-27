from django.contrib import admin
from django.conf import settings

from .models import RandomInt


# Таблица кастомизации профиля пользователя:
@admin.register(RandomInt)
class AccountAdmin(admin.ModelAdmin):
    fields = ['random_number', 'created']
    list_display = ['id', 'random_number', 'created']
