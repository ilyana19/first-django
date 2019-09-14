"""first_web_app URL Configuration

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
# from django.contrib import admin
from random import randint
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def home_page(request):
  context = {'name': 'Linda'}
  response = render(request, 'index.html', context)
  return HttpResponse(response)


def portfolio(request):
  image_urls = []
  for i in range(5):
    random_num = randint(0, 100)
    image_urls.append(
      "https://picsum.photos/400/600/?image={}".format(random_num))

  context = {'gallery_images': image_urls}
  response = render(request, 'gallery.html', context)
  return HttpResponse(response)


def about(request):
  context = {
    'skills': ['ruby', 'rails', 'python'],
    'interests': ['gaming', 'music', 'vocaloid']
  }
  response = render(request, 'about.html', context)
  return HttpResponse(response)


def favourites(request):
  context = {
    'fave_links': [
      'https://google.ca',
      'https://lindalou.ca'
    ]
  }
  response = render(request, 'links.html', context)
  return HttpResponse(response)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/', home_page),
    path('portfolio/', portfolio),
    path('about_me/', about),
    path('favourites/', favourites),
]
