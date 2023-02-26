from rest_framework import serializers
from api.models import ApiData


class ApiCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiData
        fields = ["id","tag_id", "device_id", "timestamp"]