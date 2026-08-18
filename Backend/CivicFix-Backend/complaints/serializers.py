from rest_framework import serializers
from .models import Complaint


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = [
            "id",
            "title",
            "description",
            "category",
            "latitude",
            "longitude",
            "status",
            "created_at",
            "updated_at",
        ]
