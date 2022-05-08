from django.urls import path
from user import views
urlpatterns = [
    path('users/', views.user, name='user'),
    path('login/', views.login, name='login'),
]
