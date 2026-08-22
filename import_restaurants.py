import os
import django
import csv

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

django.setup()

from restaurant_1.models import Restaurant

with open("restaurants_clean.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:

        restaurant = Restaurant.objects.create(
            name=row[0],
            address=row[1]
        )

        print(restaurant)