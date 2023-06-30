from django.db import models
from django.urls import reverse


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    res_id = models.IntegerField(unique=True)

    latitude = models.FloatField()
    longitude = models.FloatField()

    location = models.CharField(max_length=30)

    address = models.CharField(max_length=255)

    rating = models.FloatField(help_text="Rating out of 5", null=True, blank=True)

    # psuedo value, doesn't really represent if the restaurant is delivering now
    online = models.BooleanField(default=False)

    def get_absolute_url(self) -> str:
        return reverse("restaurant:list", kwargs={"restaurant_id": self.pk})

    def get_google_maps_url(self) -> str:
        return f"https://maps.google.com/?q={self.latitude},{self.longitude}"

    def __str__(self) -> str:
        return self.name
