from django.db import models


class City(models.Model):
    name_city = models.CharField(max_length=80)

    def __str__(self):
        return self.name_city


class Product(models.Model):
    name_product = models.CharField(max_length=150)

    def __str__(self):
        return self.name_product


class Client(models.Model):
    name_client = models.CharField(max_length=80)
    products = models.ManyToManyField(Product)
    cities = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_client


class Provider(models.Model):
    name_provider = models.CharField(max_length=80)
    city = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_provider
