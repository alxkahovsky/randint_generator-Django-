Описание проекта: 
1. в проекте реализовано django-приложение "accounts", содержит в себе собственную модель аккаунта, привязывает user из базовых средств авторизации djano к создаваемому аккаунту (СВЯЗЬ 1 К 1); 
Приложение позволяет зарегистрировать нового пользователя/залогиниться/разлогиниться; 
Возможность залогиниться используя github присутствует, используется библиотека social-auth-app-django; 
2. в проекте реализовано django-приложение "randint-generator" содержит в себе модель случайного числа и функцию-представление для передачи данных в шаблон; 
Генерация случайного числа происходит внутри собственного менеджера приложения "randint_generator" при выполнении команды "generator" (python3 manage.py generator), каждые 5 секунд производится перезапись числа в БД; 
Запуск команды производится по CRON у; 
Поскольку минимальное значения cron - 1 минута, команда "generator" содержит в себе итерацию; 
 
3. для обновления данных на странице используется AJAX, который опрашивает сервер каждые 0,5 секунд; 
Если пользователь не залогинился AJAX не опрашивает сервер; 
 
Список библиотек содержится в req.txt 
