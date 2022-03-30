from booking.models import Users
from rest_framework import generics
from booking.serializers import UsersSerializer



class BookingList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer



class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users
    serializer_class = UsersSerializer




