from rest_framework import serializers
from .models import CustomUser


# output serializer class for  'Mods' model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
