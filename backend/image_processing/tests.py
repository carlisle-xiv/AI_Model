import os
from pathlib import Path

from django.urls import reverse
from django.core.files import File

from rest_framework.test import APITestCase, APIClient

from .serializers import ImageSerializer


class ProcessImageViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.data = {"image": File(open(os.path.join(Path(__file__).resolve().parent.parent, "image_processing", "me.png"), "rb"))}

    def test_serializer_image_is_valid(self):
        """
        Tests that serializer is valid when image is present in request body
        returns:
        """
        serializer = ImageSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())

    def test_view_returns_a_prediction(self):
        """
        Tests that api endpoint returns a prediction
        returns:
        """
        response = self.client.post(reverse("predict_image"), data=self.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["prediction"], 1)