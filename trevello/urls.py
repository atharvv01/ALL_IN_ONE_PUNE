"""trevello URL Configuration

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
from tourist.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home, name='home'),
    path('selection/(?<pid>[0-9]+)', Selection, name='selection'),
    path('admin_login', Admin_login, name='admin_login'),
    path('administration', Administration, name='administration'),
    path('view_city', View_City, name='view_city'),
    path('view_category', View_Category, name='view_category'),
    path('add_category', Add_Category, name='add_category'),
    path('add_city', Add_City, name='add_city'),
    path('add_places', Add_Places, name='add_places'),
    path('map', Map, name='map'),
    path('about', About, name='about'),
    path('contact', Contact, name='contact'),
    path('logout', Logout_admin, name='logout'),
    path('view_places', View_Places, name='view_places'),
    path('delete_city/(?<pid>[0-9]+)', delete_City, name='delete_city'),
    path('edit_place/(?<pid>[0-9]+)', Edit_Place, name='edit_place'),
    path('delete_place/(?<pid>[0-9]+)', delete_Place, name='delete_place'),
    path('delete_category/(?<pid>[0-9]+)', delete_Category, name='delete_category'),
    path('places/(<str:num>)', city_places, name='places'),
    path('user_query',user_query,name='user_query'),
    path('delete_query/<int:pid>',delete_query, name='delete_query'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
