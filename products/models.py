from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=1024)
    en_name = models.CharField(max_length=1024, null=True)

    description = models.TextField(null=True)
    en_description = models.TextField(null=True)

    images_list = models.JSONField()
    into_photos = models.JSONField(null=True)

    length = models.FloatField(null=True)
    width = models.FloatField(null=True)
    displacement = models.FloatField(null=True)
    passengers = models.IntegerField(null=True)
    max_load = models.FloatField(null=True)

    spec = models.FileField(null=True)
    en_spec = models.FileField(null=True)

    def __str__(self):
        return self.name


 