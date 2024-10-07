from django.urls import path
from .views.translation import translate
from .views.wordoftheday import dailyWord
from .views.resources import resources

urlpatterns = [
    path("translate/", translate, name="translate"),
    path("dailyWord/", dailyWord, name="dailyWord" ),
    path("resources/", resources, name="resources")
]