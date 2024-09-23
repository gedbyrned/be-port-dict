from django.urls import path
from .views.translation import translate
from .views.wordoftheday import dailyWord

urlpatterns = [
    path("translate/", translate, name="translate"),
    path("dailyWord/", dailyWord, name="dailyWord" )
]
