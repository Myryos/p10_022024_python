from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 
                  'can_be_contacted', 
                  'can_be_shared', 
                  'age', 'created_time']
    def create(self, validated_data):
        if int(validated_data['age']) <= 15 :
            validated_data['can_be_contacted'] = False
            validated_data['can_be_shared'] = False
        return User.objects.create_user(**validated_data)
