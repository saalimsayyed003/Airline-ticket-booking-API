from django.contrib import admin
from django.urls import path,include
from booking.views import BookingList,BookingDetail

urlpatterns = [
    path('api/booking', BookingList.as_view()),
    path('api/booking/<int:pk>',BookingDetail.as_view()),
    path('', include('booking.urls')),

]
