from django.urls import path
from . import views
from django.conf import settings

app_name = 'randint_generator'

urlpatterns = [
    path('', views.show_randint, name='home'),
    ]