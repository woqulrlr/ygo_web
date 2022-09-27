from django.urls import path

from . import views

app_name = 'ygo'
urlpatterns = [
    # http://127.0.0.1:8000/ygo/
    path('', views.index),
    # http://127.0.0.1:8000/ygo/card_id/read/
    path('read/', views.read),
]