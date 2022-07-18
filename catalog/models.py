from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}, {self.age}"


class Place(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.country}, {self.city}, {self.address}"


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    place = models.OneToOneField(Place, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.place}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    price = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.title}, {self.price}"
