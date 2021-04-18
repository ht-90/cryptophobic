from django.contrib import admin

from . import models


@admin.register(models.Coin)
class CoinAdmin(admin.ModelAdmin):
    pass
