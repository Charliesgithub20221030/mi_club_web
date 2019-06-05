"""mis_club URL Configuration

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
from HR import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('index/',views.index),
    path('accounts/login/',views.index),
    path('about/',views.about),
    path('job/',views.job),
    path('jobview/<int:jid>/',views.job_view),
    path('company_login/',views.company_login),
    path('company_login_action/',views.company_login_action),
    path('company_signup/',views.company_signup),
    path('company_signup_action/',views.company_signup_action),
    path('member_login/',views.member_login),
    path('member_login_action/',views.member_login_action),
    path('member_signup/',views.member_signup),
    path('member_signup_action',views.member_signup_action),
    
]
