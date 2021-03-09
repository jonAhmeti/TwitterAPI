from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Entities)
admin.site.register(models.Hashtag)
admin.site.register(models.Place)
admin.site.register(models.Symbol)
admin.site.register(models.Tweet)
admin.site.register(models.Url)
admin.site.register(models.User)
admin.site.register(models.UserMentions)