from django.urls import path

from dish import views

app_name = "dish"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("dish/<int:dish_id>/", views.DishDetailView.as_view(), name="detail"),
]
