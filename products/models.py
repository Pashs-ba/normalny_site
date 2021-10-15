from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField(null=True)
    images_list = models.JSONField()
    length = models.FloatField(null=True)
    width = models.FloatField(null=True)
    displacement = models.FloatField(null=True)
    passengers = models.IntegerField(null=True)
    max_load = models.FloatField(null=True)

    def __str__(self):
        return self.name


 