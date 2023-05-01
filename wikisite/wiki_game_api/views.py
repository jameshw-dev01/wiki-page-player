from django.shortcuts import render
from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse
from wiki_game_api.game_src.wiki_game import wiki_game
import json

# Create your views here.
def game_request(request: HttpRequest):
    wiki_start_link = request.GET.get("start")
    wiki_end_link = request.GET.get("end")
    if wiki_start_link is None or wiki_end_link is None:
        return HttpResponseBadRequest("Argument is missing")
    else:
        try:
            game_data = wiki_game(wiki_start_link, wiki_end_link)
            return JsonResponse(game_data)
        except:
            return HttpResponseBadRequest("Something went wrong")
