import os
import django
import csv

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

django.setup()

from restaurant_1.models import Chef, Restaurant, Dish

with open("dishes_relationship.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        chef = Chef.objects.get(name=row["chef"])
        restaurant = Restaurant.objects.get(
            name=row["restaurant"]
        )

        dish = Dish.objects.create(
            name=row["name"],
            price=row["price"],
            chef=chef,
            restaurant=restaurant
        )

        print(dish)
