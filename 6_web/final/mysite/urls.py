"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('input/', views.input, name='input'),
    path('input/similar_ply', views.similar_ply, name='similar_ply'),
    path('loading/', views.loading, name='loading'),
    path('loading/recAI', views.recAI, name='recAI'),
    path('loading/imageAI', views.imageAI, name='imageAI'),
    path('output/', views.output, name='output'),
    path('output/like_ply', views.like_ply, name='like_ply'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)