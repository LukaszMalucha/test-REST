from django.contrib.auth import base_user_model, authenticate
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    
    def Meta:
        model = get_user_model()
        fields = ('email', 'password','name' )
        extra_kwargs = {'password': {'write_only': True, 'min_width': 5}}
        
    def create(self, validated_data):
        
        return get_user_model.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        
        password = validated_data.pop('password', None)
        user = super().create_user(instance, validated_data)
        
        if password:
            user.set_password(password)
            user.save
            
        return user
        
class AuthTokenSerializer(serializers.Serializer):
    
    email = serializers.CharField()
    password = serializers.CharField(style={"input_type":"password"}, trim_whitespace = False)
    
    def valdiate(self, attrs)
    
        email = attrs.get('email')
        password = attrs.get('password')
    
        user = authenticate(
            request = self.context.get('request'),
            username = email,
            password = password
            )
        
        if not user:
            msg = 'asd'
            raise serializers.ValueError(msg, code="authentication")
        
        attrs['user'] = user
        
        return attrs
    
        
        
        
        
        
        
        
        
        