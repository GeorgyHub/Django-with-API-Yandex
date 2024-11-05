from django.urls import path, include
from .views import home, register, login, logout

urlpatterns = [
    path('', home, name='index'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='Logout'),
]