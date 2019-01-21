from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Creates a User instance from the validated_data, that contains the deserialized values
        :param validated_data: Dictionary with user data
        :return: User object
        """

        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        """
        Updates a instance of User from validated_data
        :param instance: User object to update
        :param validated_data: Dictionary with new User values
        :return: Updated User
        """
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, data):
        """
        Validates if username already exists
        :param data: username
        :return: data
        """
        users = User.objects.filter(username=data)

        # Si estoy creadno (no hay instancia) comprobar si hay usuarios con ese username
        if len(users) != 0 and not self.instance:
            raise serializers.ValidationError("Username already exists!")

        # Si estoy actualizando, el nuevo username es diferente al de la instancia (esta cambiando username)
        # y existen usuarios con ese username

        elif self.instance and self.instance.username != data and len(users) != 0:
            raise serializers.ValidationError("Username already exists!")
        else:
            return data
