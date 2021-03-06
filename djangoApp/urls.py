"""djangoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import login, logout
from user_auth.views import signup, my_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('boards/', include('board.urls')),
    path('curation/', include('curation.urls')),

    path('login/', login, kwargs={'template_name': 'user_auth/login.html'}, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('my_page/', my_page, name='my_page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
