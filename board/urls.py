from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('home', views.home, name='home'),
    path('create', views.create_board, name='create'),
    path('<int:board_id>', views.detail, name='detail'),
]