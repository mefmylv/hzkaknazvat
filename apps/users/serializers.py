from rest_framework import serializers

from apps.users.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id',  'first_name', 'last_name','email', 'username',  'age', 'direction','balance', 'wallet')

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, write_only=True)
    confirm_password = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = Users
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'direction', 'password', 'confirm_password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({'Пароль':'Пароли отличаются'})
        elif len(password) < 8:
            raise serializers.ValidationError({'Пароль':'Длина пароля не меньше 8'})
        return self.create

    def create(self, validate_data):
        user = Users.objects.create(
            username=validate_data['username'],
            first_name=validate_data['first_name'],
            last_name=validate_data['last_name'],
            email=validate_data['email'],
            age=validate_data['age'],
            direction=validate_data['direction'],
            password=validate_data['password']
        )
        user.set_password(validate_data['password'])
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('username', 'age', 'direction', 'password', 'confirm_password')  


