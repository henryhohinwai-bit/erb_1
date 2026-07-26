import os
import django
import csv

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

django.setup()

from restaurant_1.models import Chef

with open("new_chefs.csv") as file:

    reader = csv.DictReader(file)

    for row in reader:

        chef, created = Chef.objects.get_or_create(
            name=row["name"],
            email=row["email"]
        )

        if created:
            print("CREATED:", chef.name)

        else:
            print("ALREADY EXISTS:", chef.name)

print("Import completed")
