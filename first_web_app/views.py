from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def root(request):
  return HttpResponseRedirect('home')

def home_page(request):
  context = {'name': 'Linda'}
  response = render(request, 'index.html', context)
  return HttpResponse(response)

def gallery(request):
  return HttpResponseRedirect('/portfolio')

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