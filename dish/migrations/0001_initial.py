# Generated by Django 4.2.2 on 2023-06-21 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dish",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("onwards_tag", models.BooleanField(default=False)),
                ("price", models.DecimalField(decimal_places=2, max_digits=7)),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dishes",
                        to="restaurant.restaurant",
                    ),
                ),
            ],
        ),
    ]