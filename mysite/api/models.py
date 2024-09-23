from django.db import models

# Create your models here.

# Model to store words in both languages
class Word(models.Model):
    portuguese_word = models.CharField(max_length=100)
    english_word = models.CharField(max_length=100)
    english_definition = models.TextField()

    def __str__(self):
        return f"{self.portuguese_word} - {self.english_word} - {self.english_definition}"
