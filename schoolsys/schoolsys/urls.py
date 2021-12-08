"""schoolsys URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from schoolsys import settings

urlpatterns = [
    path('',include('students.urls')),
    path('students/', include('students.urls')),
    path('', include('localities.urls')),
    path('localities/', include('localities.urls')),
    path('setups/', include('setups.urls')),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
    path('studentmanager/', include('studentmanager.urls')),
    path('useradmin/', include('useradmin.urls')),
    path('usertype/', include('usertype.usertype.urls')),
    path('staff/', include('staff.urls')),
    path('exams/', include('exams.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


