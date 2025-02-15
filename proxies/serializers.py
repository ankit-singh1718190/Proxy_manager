from rest_framework import serializers
from .models import ProxyNode

class ProxyNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProxyNode
        fields = '__all__'