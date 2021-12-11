from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=30, null=True)


    def __str__(self):
        return self.cat_name

class Select_City(models.Model):
    city_name = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.city_name

class Places(models.Model):
    select_city = models.ForeignKey(Select_City, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.FileField(null=True)
    place_name = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=30, null=True)
    rating = models.IntegerField(null=True)

    def __str__(self):
        return self.select_city.city_name


class tblContact(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)
    emailid = models.CharField(max_length=60)
    subject = models.CharField(max_length=300)
    def __str__(self):
        return self.firstname
