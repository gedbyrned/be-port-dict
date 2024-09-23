from django.urls import reverse
from rest_framework.test import APITestCase
from api.models import Word  
from freezegun import freeze_time

class WordOfTheDayTests(APITestCase):

    def setUp(self):
        self.url = reverse("dailyWord")  # Adjust the URL name as needed
        # Create some sample words in the database
        self.word1 = Word.objects.create(portuguese_word="casa", english_word="house", english_definition="a building for human habitation.")
        self.word2 = Word.objects.create(portuguese_word="carro", english_word="car", english_definition="a road vehicle, typically with four wheels.")
        self.word3 = Word.objects.create(portuguese_word="gato", english_word="cat", english_definition="a small domesticated carnivorous mammal.")

    def test_get_random_word(self):
        """Test if a random word is returned successfully."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('portuguese_word', response.data)
        self.assertIn('english_word', response.data)
        self.assertIn('english_definition', response.data)

    def test_word_fields(self):
        """Test if the correct fields are returned."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('portuguese_word' in response.data)
        self.assertTrue('english_word' in response.data)
        self.assertTrue('english_definition' in response.data)

    def test_cache_word_of_the_day(self):
        """Test that the same word is returned for multiple requests within the same day."""
        
        # Freeze time at a specific date, e.g., "2024-09-22"
        with freeze_time("2024-09-22"):
            response1 = self.client.get(self.url)
            self.assertEqual(response1.status_code, 200)
            word_of_the_day = response1.data

            response2 = self.client.get(self.url)
            self.assertEqual(response2.status_code, 200)
            self.assertEqual(response2.data, word_of_the_day)

        # Simulate moving to the next day using freezegun
        with freeze_time("2024-09-23"):
            response3 = self.client.get(self.url)
            self.assertEqual(response3.status_code, 200)
            self.assertNotEqual(response3.data, word_of_the_day)

     
    def test_invalid_url(self):
        """Test that a 404 is returned for an invalid URL."""
        invalid_url = reverse("dailyWord") + "invalid/"  # Append invalid to URL
        response = self.client.get(invalid_url)
        self.assertEqual(response.status_code, 404)

    def test_malformed_request(self):
        """Method not allowed 405."""
        response = self.client.post(self.url, data={}, format="json")  # Sending an unexpected request method
        self.assertEqual(response.status_code, 405)  