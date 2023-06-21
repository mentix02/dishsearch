import csv
import json
import argparse
from decimal import Decimal

from django.core.management.base import BaseCommand, CommandParser

from dish.models import Dish
from restaurant.models import Restaurant


class Command(BaseCommand):
    """
    Custom management command to import restaurants from a CSV file.
    """

    help = "Load restaurants from a CSV file"

    def add_arguments(self, parser: CommandParser) -> None:
        return parser.add_argument(
            "csv_file",
            type=argparse.FileType("r"),
            help="CSV file with restaurant data to import",
        )

    def _create_dish(
        self, dish_name: str, price_str: str, restaurant: Restaurant
    ) -> Dish:
        price_split = price_str.split()

        price = Decimal(price_split[0])
        onwards_tag = len(price_split) > 1

        return Dish(
            price=price,
            name=dish_name,
            restaurant=restaurant,
            onwards_tag=onwards_tag,
        )

    def handle(self, *args, **options) -> None:
        reader = csv.reader(options["csv_file"])
        next(reader)  # skip the header row

        res_count = dish_count = 0

        for row in reader:
            res_id, name, location, menu, lat_long, details = row

            latitude, longitude = tuple(map(float, lat_long.split(",")))

            # for reasons unknown, some restaurants don't have a details column
            # so we have to handle that with this hacky manual dict creation
            menu, details = json.loads(menu), json.loads(details) if details else {
                "is_delivering_now": 0,
                "location": {"address": ""},
                "user_rating": {"aggregate_rating": None},
            }

            rating = details["user_rating"]["aggregate_rating"]

            restaurant = Restaurant.objects.create(
                name=name,
                res_id=res_id,
                location=location,
                latitude=latitude,
                longitude=longitude,
                address=details["location"]["address"],
                rating=float(rating) if rating else None,
                online=bool(details["is_delivering_now"]),
            )

            dishes = [
                self._create_dish(dish_name, price_str, restaurant)
                for dish_name, price_str in menu.items()
            ]

            Dish.objects.bulk_create(dishes)

            res_count += 1
            dish_count += len(dishes)

        self.stdout.write(
            self.style.SUCCESS(
                f"successfully loaded {res_count} restaurants & {dish_count} dishes"
            )
        )
