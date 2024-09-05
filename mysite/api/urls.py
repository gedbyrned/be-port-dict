from django.urls import path
from .views import translate_english

urlpatterns = [
    path("translate/", translate_english, name="translate_english"),
]
