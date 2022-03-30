from rest_framework import serializers
from booking.models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['From','To','Departure_date','Return_date','Class']