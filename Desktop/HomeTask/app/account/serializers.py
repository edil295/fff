from rest_framework import serializers

from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20, write_only=True)
    password_2 = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = Author
        fields = ['username', 'password', 'password_2']

    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError('Пароли должны совпадать')
        return data

    def create(self, validated_data):
        try:
            author = Author(username=validated_data['username'])
            author.set_password(validated_data['password'])
            author.save()
            return author
        except Exception as e:
            raise serializers.ValidationError(f'Не удалось создать пользователя. {e}')

