from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.insert_data),
    path('select', views.select_data),
]