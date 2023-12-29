from rest_framework import serializers


class ErrorSerializer(serializers.Serializer):
    fa = serializers.CharField()
    en = serializers.CharField()
    ar = serializers.CharField()
    ru = serializers.CharField()
    tr = serializers.CharField()
