from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Contactlist.objects.all()
    serializer_class = ContactlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new contactlist."""
        serializer.save()

