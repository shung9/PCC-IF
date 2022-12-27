from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'


urlpatterns = [
    path('login/', views.login, name="login"),
    path('registrar/', views.registrar, name="registrar"),
    path('logout/', views.logout, name="logout"),

    path('redefinir-senha/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('redefinição-enviada/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('redefinir/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('redefinição-completa/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]


