"""BitirmePROJE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from appMy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('Products/', Products, name='Product'),
    path('About/', About, name='About'),
    path('Contact/', ContactUs, name='ContactUs'),
    path('Shop/', Shop, name='Shop'),
    path('ShopDetail/<slug>/', ShopDetail, name='ShopDetail'),
    path('ShopBasketDelete/<sid>/', ShopBasketDelete, name='ShopBasketDelete'),
    path('ShopBasket/', ShopBasket, name='ShopBasket'),


    # USER
    path('login/',loginUser, name='loginUser'),
    path('logout/',logoutUser, name='logoutUser'),
    path('register/',registerUser, name='registerUser'),
    path('changePassword/', changePassword, name='changePassword'),
    path('Profil/', profilUser, name='profilUser'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
