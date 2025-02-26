"""
URL configuration for codestar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# codestar/urls.py (or the main URL configuration file)

from django.contrib import admin
from django.urls import path
from blog.views import hello_blog, home  # Import the new view function

urlpatterns = [
    path('', home, name='home'),  # Add the new URL pattern for the root URL
    path('blog/', hello_blog, name='blog'), 
    path('admin/', admin.site.urls),
]