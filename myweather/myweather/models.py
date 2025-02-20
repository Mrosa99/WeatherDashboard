from django.db import models
from django.contrib.auth.models import User


class weatherSearch(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="weather_searches",
        null=True,
        blank=True,
    )

    city = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    precipitation = models.IntegerField()
    humidity = models.IntegerField()
    forecast = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Weather search for {self.city} on {self.date}"
