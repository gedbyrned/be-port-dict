from django.db import models

# Create your models here.

# Model to store words in both languages
class Word(models.Model):
    portuguese_word = models.CharField(max_length=100)
    english_word = models.CharField(max_length=100)
    english_definition = models.TextField()

    def __str__(self):
        return f"{self.portuguese_word} - {self.english_word} - {self.english_definition}"
    

class Resources(models.Model):
    resource_name = models.CharField(max_length=300)
    resource_type = models.CharField(max_length=100) 
    resource_author = models.CharField(max_length=100, blank=True, null=True) 
    resource_description = models.CharField(blank=True, null=True) 
    resource_level = models.CharField(max_length=100, blank=True, null=True) 
    resource_language = models.CharField(max_length=100, blank=True, null=True) 
    resource_url = models.URLField(blank=True, null=True)
    resource_image = models.ImageField(upload_to='resources/', blank=True, null=True)

    def __str__(self):
        return self.resource_name