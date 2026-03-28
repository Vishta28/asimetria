from . import views
from django.urls import path

urlpatterns = [
    path('callback', views.callback_page, name='callback')
]