from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'<int:post_id>/', views.post_detail, name='detail')
]