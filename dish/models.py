import random

from django.db import models
from django.urls import reverse
from django.db.models.query import QuerySet

from restaurant.models import Restaurant


class DishManager(models.Manager):
    def search(self, query: str) -> QuerySet:
        """
        Convience method to "search" for dishes with __icontains
        and sort by restaurant's rating.
        """
        return self.filter(name__icontains=query).order_by("-restaurant__rating")


class Dish(models.Model):
    name = models.CharField(max_length=255)

    onwards_tag = models.BooleanField(default=False)

    price = models.DecimalField(max_digits=7, decimal_places=2)

    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="dishes"
    )

    objects = DishManager()

    def get_absolute_url(self) -> str:
        return reverse("dish:detail", kwargs={"dish_id": self.pk})

    def get_other_restaurant_dishes(self, n: int = 3) -> models.QuerySet:
        """
        Convience method to get other dishes from the same restaurant as
        a sorry excuse for a recommendation system. Get random dishes
        in the 1 to n sliding window.
        """
        return (
            Dish.objects.filter(restaurant=self.restaurant)
            .exclude(pk=self.pk)
            .order_by("?")[:n]
        )

    def __str__(self) -> str:
        return self.name
