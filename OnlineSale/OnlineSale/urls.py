"""OnlineSale URL Configuration

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
from django.urls import path,include
from django.views.generic import TemplateView
from customerapp import urls
from adminapp import views
from adminapp.models import Admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminlogin',views.adminLogin,name="adminlogin"),
    path('validate/',views.validate,name="validate"),
    path('addmerchant/',views.addmerchant,name="addmerchant"),
    path('viewmerchant/',views.viewmerchant,name="viewmerchant"),
    path('deletemerchant/',views.deletemerchant,name="deletemerchant"),
    path('addmc/',views.addmc,name="addmc"),
    path('delmerc/',views.deletemerchant,name="delmerc"),
    path('login/',views.Login.as_view()),
    path('addproduct/',views.Addproduct.as_view()),
    path('viewproduct/',views.Viewproduct.as_view()),
    path('changepwd/',views.Changepwd.as_view()),
    path('updateproduct/<int:pk>/',views.UpdateProduct.as_view()),
    path('updateprod/',views.UpdateProduct.as_view()),
    path('deleteproduct/<int:pno>/',views.DeleteProduct.as_view()),
    path('customerapp/',include('customerapp.urls'))

]
