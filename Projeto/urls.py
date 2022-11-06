from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('turmas/', include('turmas.urls')),
]


