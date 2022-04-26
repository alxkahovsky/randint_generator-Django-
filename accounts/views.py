from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm, UserEditForm
from .models import Account

UserModel = get_user_model()


def register(request):
    if request.user.is_authenticated == False:
        if request.method == 'POST':
            # Создается объект формы с данными:
            user_form = UserRegistrationForm(request.POST)
            # Если форма валидна, то:
            if user_form.is_valid():
                # Создаем нового пользователя, но в БАЗЕ он НЕ СОХРАНЕН!
                new_user = user_form.save(commit=False)
                # Зададим пользователю пароль для его аккаунта:
                new_user.set_password(user_form.cleaned_data['password'])
                # Сохраним пользователя в БАЗЕ:
                new_user.save()
                # Создание профиля пользователя:
                Account.objects.create(user=new_user)
                context_done = {
                    'new_user': new_user,
                }
                return render(request, 'accounts/register_done.html', context_done)
            else:
                return render(request, 'accounts/register_failed.html')
        else:
            user_form = UserRegistrationForm()
        context = {
            'user_form': user_form,
        }
        return render(request, 'accounts/registration.html', context)
    else:
        return redirect('randint_generator:index')
