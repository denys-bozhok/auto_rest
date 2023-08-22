from django.contrib import admin

from . import models


admin.site.register(models.Auto)
admin.site.register(models.AutoPassport)
admin.site.register(models.Owner)
