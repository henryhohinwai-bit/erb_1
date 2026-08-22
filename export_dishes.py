import os
import django
import csv

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

django.setup()

from restaurant_1.models import Dish

output_file = open(
    "dishes_export.csv",
    "w",
    newline=""
)

writer = csv.writer(output_file)

writer.writerow(
    ["name", "price", "chef", "restaurant"]
)

for dish in Dish.objects.all():
    writer.writerow([
        dish.name,
        dish.price,
        dish.chef.name,
        dish.restaurant.name
    ])

output_file.close()

print("dishes_export.csv created")

