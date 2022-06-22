from pyexpat import model
from tkinter.ttk import Style
from rest_framework import serializers, validators
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .validators import LessThanValidator, GreaterThanValidator
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    username = serializers.CharField(validators=[LessThanValidator(3), GreaterThanValidator(32),
                                                validators.UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    email = serializers.EmailField(style={'input_type': 'email'}, write_only=True,
                                    validators=[validators.UniqueValidator(queryset=User.objects.all())])

    def create(self, validated_data):
        if validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError({'error': "Passwords doesn't match"})
        
        validated_data['password'] = make_password(validated_data['password'])

        validated_data.pop('password2', None)
        return super().create(validated_data)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_messages = {
        'bad_token': ('Token is not exist')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(token=self.token).blacklist()
        except TokenError:
            self.fail('bad_token')

