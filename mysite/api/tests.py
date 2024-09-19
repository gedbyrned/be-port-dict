from django.urls import reverse
from rest_framework.test import APITestCase


class TranslationTests(APITestCase):

    def setUp(self):
        self.url = reverse("translate")

    def test_translate_hello(self):
        data = {"q": "hello", "source": "en", "target": "pt"}  # English to Portuguese
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.data["translated_text"], "olá")

    def test_translate_thank_you(self):
        data = {"q": "thank you", "source": "en", "target": "pt"}  # English to Portuguese
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.data["translated_text"], "obrigado")

    def test_translate_love(self):
        data = {"q": "love", "source": "en", "target": "pt"}  # English to Portuguese
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.data["translated_text"], "amor")

    def test_translate_olá(self):
        data = {"q": "tudo", "source": "pt", "target": "en"}  # Portuguese to English
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.data["translated_text"], "everything")

    def test_translate_obrigado(self):
        data = {"q": "obrigado", "source": "pt", "target": "en"}  # Portuguese to English
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.data["translated_text"], "thank you")

    def test_translate_amor(self):
        data = {"q": "amor", "source": "pt", "target": "en"}  # Portuguese to English
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.data["translated_text"], "love")

    def test_translate_empty_string(self):
        data = {"q": "", "source": "en", "target": "pt"}  # if passed empty string 
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.data["translated_text"], "")

    def test_translate_unknown_word(self):
        data = {"q": "43423fsaf", "source": "en", "target": "pt"}  # if word unknown
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.data["translated_text"], "")
