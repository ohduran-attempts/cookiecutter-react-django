from django.urls import path
from . import views

urlpatterns = [
    path('char_count/', views.char_count),
]