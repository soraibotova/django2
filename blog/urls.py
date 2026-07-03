from django.urls import path
from blog.views import home, contact

urlpatterns = [
    path('home/',home),
    path('contact/',contact),
]