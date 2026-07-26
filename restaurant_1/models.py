from django.db import models


class Chef(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(
    max_digits=8,
    decimal_places=2
    )
    # relational to chef
    chef = models.ForeignKey(
        Chef,
        on_delete=models.CASCADE
    )
    # relational to restaurant
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.name

