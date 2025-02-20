from django.db import models


class weatherSearch(models.Model):

    city = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    precipitation = models.IntegerField()
    humidity = models.IntegerField()
    forecast = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Weather search for {self.city} on {self.date}"
