"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# to use include function we need to import here.
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # address is app.  include all urls we have in our app level so, include function and pass it our app name which is 'firstapp.urls'and this is going to get urls file from our application.
    path('app/', include('firstapp.urls'))

]
# to access our different views we can use following urls http://<localhost>/app/<path_in_view>
# http://<localhost>/app/function   helloworld view
# http://<localhost>/app/class      helloethopia view
