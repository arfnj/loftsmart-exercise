from django.test import TestCase
from .models import Contactlist
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):
    """This class defines the test suite for the contactlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.contactlist_name = "Write world class code"
        self.contactlist = Contactlist(name=self.contactlist_name)

    def test_model_can_create_a_contactlist(self):
        """Test the contactlist model can create a contactlist."""
        old_count = Contactlist.objects.count()
        self.contactlist.save()
        new_count = Contactlist.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.contactlist_data = {'name': 'Bort'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json")

    def test_api_can_create_a_contactlist(self):
        """Test the api has contact creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)