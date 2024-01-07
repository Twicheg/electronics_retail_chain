from rest_framework import serializers


class UpdateValidator:
    def __call__(self, value):
        if "debt" in list(value):
            raise serializers.ValidationError("Запрещено менять задолженность перед поставщиком")
