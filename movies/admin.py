from django.contrib import admin
from .models import SaveAPITokenModel, userMovieSuggestionsModel, userSearchHistoryModel, userMovieSaveModel
# Register your models here.
admin.site.register(SaveAPITokenModel)
admin.site.register(userMovieSuggestionsModel)
admin.site.register(userSearchHistoryModel)
admin.site.register(userMovieSaveModel)