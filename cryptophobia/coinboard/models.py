from django.db import models


class Coin(models.Model):
    id = models.IntegerField(
        primary_key=True,
        auto_created=True,
    )
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name="Coin Name",
    )
    ticker = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        verbose_name="Coin Alias",
    )
    address = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="Coin Address",
    )

    def __str__(self):
        return self.name
