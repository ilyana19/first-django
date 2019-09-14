from django.urls import path
from first_web_app.views import root, home_page, gallery, portfolio, about, favourites

urlpatterns = [
  path('', root),
  path('home/', home_page),
  path('gallery/', gallery),
  path('portfolio/', portfolio),
  path('about_me/', about),
  path('favourites/', favourites),
]
