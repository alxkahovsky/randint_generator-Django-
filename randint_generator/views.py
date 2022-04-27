from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
import random
import time
from .models import RandomInt


def show_randint(request):
    if request.user.is_authenticated:
        username = request.user.username
        random_ints = RandomInt.objects.all()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'rand_number': random_ints[0].random_number}, status=200)
        else:
            context = {
                'number': random_ints[0].random_number,
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

