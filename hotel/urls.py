
from django.urls import path
from .views import HotelApiView


urlpatterns = [
    path('hotels/', HotelApiView.as_view(), name='hotel-list'),
]