from django.urls import path
from first_web_app.views import home_page, portfolio, about, favourites

urlpatterns = [
    path('home/', home_page),
    path('portfolio/', portfolio),
    path('about_me/', about),
    path('favourites/', favourites),
]
