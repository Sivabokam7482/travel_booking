from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('travels/', views.travel_list, name='travel_list'),
    path('book/<int:travel_id>/', views.book_travel, name='book_travel'),
    path('bookings/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),


]
