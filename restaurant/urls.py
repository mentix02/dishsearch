from django.urls import path

from restaurant import views

app_name = "restaurant"

urlpatterns = [
    path(
        "<int:restaurant_id>/",
        views.RestaurantDishListView.as_view(),
        name="list",
    ),
]
