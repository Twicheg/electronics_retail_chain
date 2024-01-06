from rest_framework import serializers

from main.models import ChainLink


class ChainListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChainLink
        fields = '__all__'


class ChainCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChainLink
        fields = ("id", "title", "email", "country", "city", "street", "house_number", "product_name", "product_model",
                  "exit_date", "provider", "debt", "company")
        validators = []