from email.mime import application
from order import views
from django.urls import path


urlpatterns = [
    path('shops/', views.shop, name='shops'),
    path('menus/<int:shop>', views.menu, name='menu'),
    path('order/', views.order, name='order'),
]