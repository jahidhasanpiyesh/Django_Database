from django.urls import path
from .views import index, delete, create

urlpatterns = [
    path('', index, name='index'),
    path('delete/<int:id>/', delete, name='delete'),
    path('create/', create, name='create'),
]
