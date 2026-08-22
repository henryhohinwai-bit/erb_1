import os
import django
import csv

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

django.setup()

from restaurant_1.models import Restaurant

output_file = open(
    "restaurants_export.csv",
    "w",
    newline=""
)

writer = csv.writer(output_file)

writer.writerow(["name", "address"])

for restaurant in Restaurant.objects.all():
    writer.writerow([
        restaurant.name,
        restaurant.address
    ])

output_file.close()

print("restaurants_export.csv created")