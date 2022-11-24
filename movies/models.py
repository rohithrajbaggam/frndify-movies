from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class SaveAPITokenModel(models.Model):
    api_key = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    lastupdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.api_key

class userMovieSaveModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="user_movie_save_list")
    imdbid = models.CharField(max_length=500, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=500, null=True, blank=True)
    is_saved = models.BooleanField(default=False)

    timestamp = models.DateTimeField(auto_now_add=True)
    lastupdated = models.DateTimeField(auto_now=True)
class userMovieSuggestionsModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="user_movie_suggestions")
    title = models.CharField(max_length=500, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=500, null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    lastupdated = models.DateTimeField(auto_now=True)


class userSearchHistoryModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="user_search_history_fkey")
    url = models.CharField(max_length=500, null=True, blank=True)
    search_keyword = models.CharField(max_length=500, null=True, blank=True)
    api_key = models.CharField(max_length=500, null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    lastupdated = models.DateTimeField(auto_now=True)