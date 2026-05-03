from django.urls import path
from . import views

urlpatterns = [
    path('reservations/', views.reservation_list),
    path('customers/', views.customer_list),
]