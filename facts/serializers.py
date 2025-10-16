from rest_framework import serializers
from .models import Fact

class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = ["id", 'text', 'created_at']