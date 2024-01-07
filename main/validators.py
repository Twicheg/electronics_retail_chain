from rest_framework import serializers


class UpdateValidator:
    def __call__(self, value):
        if "debt" in value:
            raise serializers.ValidationError("Запрещено меня задолженность перед поставщиком")
