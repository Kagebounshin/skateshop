from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.sub_form, name='sub_form'),
]
