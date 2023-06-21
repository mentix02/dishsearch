from typing import Optional

from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView

from dish.models import Dish


class HomeView(ListView):
    model = Dish
    paginate_by = 10
    context_object_name = "dishes"
    template_name = "dish/list.html"

    def get_queryset(self) -> QuerySet:
        query: Optional[str] = self.request.GET.get("q")
        if query:
            return Dish.objects.search(query).select_related("restaurant")
        return Dish.objects.none()


class DishDetailView(DetailView):
    model = Dish
    pk_url_kwarg = "dish_id"
    context_object_name = "dish"
    template_name = "dish/detail.html"
