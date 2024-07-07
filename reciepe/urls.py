"""
URL configuration for reciepe project.

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
from vege.views import *

urlpatterns = [

    path('receipes/', receipes),
    path('admin/', admin.site.urls),
    path('delete_receipe/<id>/',delete_receipe),
    path('update_receipe/<id>/',update_receipe,name="update_receipe"),
    path('login_page/',login_page,name="login_page"),
    path('logout_page/',logout_page,name="logout_page"),
    path('register/',register,name="register"),
]
