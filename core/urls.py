from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('toggle-chat/', views.toggle_chat, name='toggle_chat'),
]
