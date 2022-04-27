from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
import random
import time
from .models import RandomInt


def show_randint(request):
    if request.user.is_authenticated:
        username = request.user.username
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            number = 0
            rand_number = number
            while number == rand_number:
                rand_number = random.randint(0, 9999999)
            return JsonResponse({'rand_number': rand_number}, status=200)
        else:
            context = {
                'number': random.randint(0, 9999999),
                'login': True,
                'username': username
            }
            return render(request, 'randint_generator/randint_generator.html', context)
    else:
        context = {
            'number': 'Для отображения случайного числа необходимо авторизоваться',
            'login': False
        }
        return render(request, 'randint_generator/randint_generator.html', context)

