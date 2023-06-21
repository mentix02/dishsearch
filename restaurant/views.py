from typing import Any, Dict

from django.views.generic import ListView
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

from dish.models import Dish
from restaurant.models import Restaurant


class RestaurantDishListView(ListView):
    model = Dish
    paginate_by = 10
    context_object_name = "dishes"
    template_name = "dish/list.html"

    def get_queryset(self) -> QuerySet:
        # get dishes from restaurant
        return (
            Dish.objects.filter(restaurant_id=self.kwargs["restaurant_id"])
            .select_related("restaurant")
            .order_by("-restaurant__rating")
        )

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["restaurant"] = get_object_or_404(
            Restaurant, pk=self.kwargs["restaurant_id"]
        )
        return context
