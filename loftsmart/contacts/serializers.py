from rest_framework import serializers
from .models import Contactlist

class ContactlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Cucketlist
        fields = ('id', 'name', 'phone', 'image', 'country', 'cleanPhone', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')