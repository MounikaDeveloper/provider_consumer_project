"""Merchant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from merchantapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/',views.Readone.as_view(),name="index"),
    path('merchantlogin/',views.loginCheck,name="merchantlogin"),
    path('merchanthome/',views.merchantHome,name="merchanthome"),
    path('product/',views.product,name="product"),
    path('addproduct/',views.addproduct,name="addproduct"),
    path('viewproduct/',views.viewproduct,name="viewproduct"),
    path('saveproduct/',views.saveproduct,name="saveproduct"),
    path('login/',views.login,name="login"),
    path('change/',views.change,name="change"),
    path('changepwd/',views.changepassword,name="changepwd"),
    path('updateproduct/',views.updateproduct,name="updateproduct"),
    path('upd_prod/',views.upd_prod,name="upd_prod"),
    path('deleteproduct/',views.deleteproduct,name="deleteproduct")


]
