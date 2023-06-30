from django.urls import path
from . import views
#from .views import google_auth, google_auth_redirect, google_calendar

urlpatterns = [
    path('<str:codigo>', views.calendario, name="calendario"),
]
