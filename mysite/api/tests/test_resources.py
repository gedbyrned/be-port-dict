from django.urls import reverse
from rest_framework.test import APITestCase
from api.models import Resources
from django.core.files import File
import os

class ResourcesTest(APITestCase):

    def setUp(self):
        self.url = reverse("resources")
        self.resource1 = Resources.objects.create(
            resource_name="portBook",
            resource_type="text book",
            resource_author="James Fenn",
            resource_description="your standard Portuguese textbook",
            resource_level="intermediate",
            resource_language="en",
            resource_url="www.random-url.com",
            resource_image="" 
        )

    def test_upload_image_to_s3(self):
        """Test that an image can be uploaded and is accessible on S3."""
        image_path = 'api/tests/test_images/simpsons_sofa.jpg'

        self.assertTrue(os.path.isfile(image_path), f"Image file not found at path: {image_path}")

        with open(image_path, 'rb') as img:
            resource = Resources(
                resource_name="Test Resource",
                resource_type="Image Test",
            )
            resource.resource_image.save('simpsons_sofa.jpg', File(img), save=True)  # Save to S3
            resource.save()

        self.assertTrue(resource.resource_image.url.startswith('https://'), "Image URL should start with 'https://'")

    def test_invalid_resources_url(self):
        """Test that a 404 is returned for an invalid URL on the resources endpoint."""
        invalid_url = reverse("resources") + "invalid/"
        response = self.client.get(invalid_url)
        self.assertEqual(response.status_code, 404)
    
    def test_resource_name_missing(self):
        """Test that a 400 is returned when resource_name is missing."""
        # Create a resource with an empty resource_name
        Resources.objects.create(resource_name="", resource_type="Book")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 400)
        self.assertIn("resource_name and resource_type are required fields.", response.data['error'])

    def test_resource_type_missing(self):
        """Test that a 400 is returned when resource_type is missing."""
        # Create a resource with an empty resource_type
        Resources.objects.create(resource_name="Test Resource", resource_type="")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 400)
        self.assertIn("resource_name and resource_type are required fields.", response.data['error'])




