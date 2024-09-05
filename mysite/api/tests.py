from django.urls import reverse
from rest_framework.test import APITestCase


class TranslationTests(APITestCase): # setup test class which inherits APITestCase

    def setUp(self): #method in Djangos testframework that runs before each test, used to set up reusable objects
        self.url = reverse("translate_english")  # stores "translate_english" in self.url, to avoidhardcoding urls in each test, makes code cleaner.

    def test_translate_hello(self):
        data = {"q": "hello"} #sets up data payload that is sent to API 
        response = self.client.post(self.url, data, format="json") # sends post request to URL previously stored, passing as a data payload, self.client is provided by the import APITestCase and is used to simulate HTTP requests
        self.assertEqual(response.data["translated_english_text"], "olá") #ensures that "ola" is is the value in the "translated_english_text" key

    def test_translate_thank_you(self):
        data = {"q": "thank you"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.data["translated_english_text"], "obrigado")

    def test_translate_love(self):
        data = {"q": "love"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.data["translated_english_text"], "amor")

    def test_translate_empty_string(self):#logic for this test is handled in views.py 
        """Test that an empty string is translated to an empty string"""
        data = {"q": ""}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.data["translated_english_text"], "")

    def test_translate_unknown_word(self):#logic for this test is handled in views.py 
        data = {"q": "43423fsaf"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.data["translated_english_text"], "")
