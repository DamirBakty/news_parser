from rest_framework import serializers

from api import models

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'

