from django.urls import path
from . import views

urlpatterns = [
    path('available_slots/<str:date>/', views.available_slots, name='available_slots'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
]