import os
import django
import csv

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

django.setup()

from restaurant_1.models import Chef

with open(
    "chef_export.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "name",
        "email"
    ])

    for chef in Chef.objects.all():

        writer.writerow([
            chef.name,
            chef.email
        ])

print("Export completed")