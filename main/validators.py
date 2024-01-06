from rest_framework import serializers


def validate_debt(value):
    try:
        return round(float(value), 2)
    except:
        raise serializers.ValidationError("Задолженность перед поставщиком в денежном выражении с точностью до копеек")
