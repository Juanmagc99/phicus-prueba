from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.start_game, name="start_game"),
    path("play/<int:game_id>/<str:player>/<int:position>/", views.play, name="play"),
    path("details/<int:game_id>/", views.game_info, name="game_info"),
    path("all/", views.get_all, name="all_games"),
]   