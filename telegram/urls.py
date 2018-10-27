from django.urls import path

from . import views

app_name = 'telegram'
urlpatterns = [
    path('predict/', views.predict, name='predict'),
]