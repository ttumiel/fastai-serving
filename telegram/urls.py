from django.urls import path

from . import views

app_name = 'telegram'
urlpatterns = [
    path('<str:bot_token>/predict/', views.Predict.as_view(), name='predict'),
]