from django.http import JsonResponse
from ..models import Word
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random
from django.core.cache import cache
from datetime import date


@api_view(["GET"])
def dailyWord(request):
    today = date.today().isoformat()
    cache_key = f"word_of_the_day_{today}"

    word_of_the_day = cache.get(cache_key)

    if not word_of_the_day:
        # If the cache is empty or outdated, pick a new random word
        words = Word.objects.all()
        random_word = random.choice(words)

        # Store the word in the cache with a timeout of one day (86400 seconds)
        word_of_the_day = {
            "portuguese_word": random_word.portuguese_word,
            "english_word": random_word.english_word,
            "english_definition": random_word.english_definition,
        }
        cache.set(cache_key, word_of_the_day, timeout=86400)

    return Response(word_of_the_day)
