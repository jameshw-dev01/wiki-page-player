from django.urls import path

from wiki_game_api import views
urlpatterns = [
    path("api", views.game_request, name="game"),
]