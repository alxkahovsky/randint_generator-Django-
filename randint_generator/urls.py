from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', randint_generator.LoginView.as_view(), name='login'),
    path('logout/', randint_generator.LogoutView.as_view(next_page='home'), name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
    ]