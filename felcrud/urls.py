"""felcrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from keylib import views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('drf/', include('keylib.urls')),
    path('library/', views.Library_api.as_view(),name='library'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('register/', views.register,name='register'),
    path('', views.index,name='index'),
    path('addshow/', views.addshow,name="addshow"),
    path('allbooks/', views.allbooks,name="allbooks"),
    path('delete/<int:id>/', views.deletebook,name="deletebook"),
    path('<int:id>/', views.updatebook,name="updatebook"),
    path('func1/', views.func1,name="func1"),
    path('empl/', views.employee_api,name="employee_api"),
    path('empl/<int:id>', views.employee_api,name="employee_api"),
    
]
