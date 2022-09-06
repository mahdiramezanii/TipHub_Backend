from django.contrib import admin

from Tutorial_app import models

admin.site.register(models.VideoTutorial)
admin.site.register(models.Category)
admin.site.register(models.Tags)
admin.site.register(models.Comment)
admin.site.register(models.SubCategory)