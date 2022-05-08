from email.mime import application
from boss import views
from django.urls import path


urlpatterns = [
    path('orders/<int:shop>', views.order_list, name="order_list"),
    path('timeinput/', views.time_input, name="time_input"),
]