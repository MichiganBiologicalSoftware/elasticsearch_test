from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('make/', views.make, name='make'),
    path('view/<car_id>', views.view, name='view')
]