"""DBMS_MINIPROJECT URL Configuration

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
from django.urls import path
from  . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('StudentLogin',views.index),
    path('StudentLogin2',views.studentLogin),
    path('studenthome',views.home),
    path('studenthome/profile',views.profile),
    path('studenthome/doubts',views.doubts),
    path('studenthome/answers',views.answers),
    path('studenthome/contact',views.contact),
    path('logout',views.logout),
    path('studenthome/doubts/submit',views.doubtsubmit),
    path('TeacherLogin',views.teacherlogin),
    path('TeacherHome',views.teacherhome),
    path('TeacherHome/profiles',views.teacherprofile),
    path('TeacherHome/question',views.teacherquestion),
    path('TeacherHome/answered',views.teacheranswered),
    path('TeacherHome/contact',views.teachercontact),
    path('TeacherLogout',views.teacherLogout),
    path('TeacherLogin1',views.teacherindex)
]
