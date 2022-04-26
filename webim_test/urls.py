from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('', include('randint_generator.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
]
