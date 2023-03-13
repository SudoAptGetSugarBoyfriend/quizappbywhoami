from Quiz.models import QuesModel
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class QuizApiSerializer(serializers.ModelSerializer):

	class Meta:
		model = QuesModel
		fields = '__all__'

class UserLoginApiSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['username', 'password']

class RegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 'password', 'password2')
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username']
    )
    user.set_password(validated_data['password'])
    user.save()
    return user