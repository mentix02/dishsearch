from django.contrib import admin

from restaurant.models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ("name", "res_id")
    list_filter = ("online", "location")
    list_display = ("name", "res_id", "location", "address", "rating", "online")
