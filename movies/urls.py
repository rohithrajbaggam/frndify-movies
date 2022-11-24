from . import views 
from django.urls import path 

urlpatterns = [ 
    path("", views.home, name="home"),
    path("suggestions/<name>/", views.suggestionsView, name="suggestionsView"),
    path("save-movie/<imdbid>/<link>/", views.userMovieSaveView, name="userMovieSaveView"),
    path("unsave-movie/<imdbid>/", views.userMovieUnSaveView, name="userMovieUnSaveView"),
    path("history/", views.userBrowsingHistory, name="userBrowsingHistory"),
    path("search/", views.search, name="search"),
    
    # path("hostory/")
]
