"""geekshop URL Configuration

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
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path
from mainapp import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name="main"),
    path("products/", include("mainapp.categories_urls", namespace="products")),
    path('contact/', views.contact, name="contact"),
    path('admin/', admin.site.urls, name="urls"),
    path("auth/", include('django.contrib.auth.urls')),
    path("client_area/", include('authapp.urls', namespace="client_area")),
    path("basket/", include('basketapp.urls', namespace="basket")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
