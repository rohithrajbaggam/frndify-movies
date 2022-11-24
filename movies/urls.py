from . import views 
from django.urls import path 

urlpatterns = [ 
    path("", views.home, name="home"),
    path("suggestions/<name>/", views.suggestionsView, name="suggestionsView"),
    path("save-movie/<imdbid>/<link>/", views.userMovieSaveView, name="userMovieSaveView"),
    path("unsave-movie/<imdbid>/", views.userMovieUnSaveView, name="userMovieUnSaveView"),
    
    path("search/", views.search, name="search"),
]
